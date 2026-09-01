import asyncio
import io
import math
import os
from typing import BinaryIO, Callable, Optional, Union
import ftmgram
from ftmgram import raw, utils


class TurboTransfer:
    """High-speed parallel chunk download and upload engine for FTMGram."""

    @staticmethod
    async def parallel_download(
        client: "ftmgram.Client",
        location: Union["raw.types.InputFileLocation", "raw.types.InputDocumentFileLocation", "raw.types.InputPhotoFileLocation"],
        file_size: int,
        destination: Union[str, BinaryIO, io.BytesIO],
        dc_id: int,
        chunk_size: int = 1024 * 1024,  # 1 MB optimal chunk
        workers: int = 8,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
    ) -> Union[str, BinaryIO, io.BytesIO]:
        """Download file parts concurrently across multiple workers for maximum network saturation."""
        total_parts = math.ceil(file_size / chunk_size)
        downloaded_bytes = 0
        lock = asyncio.Lock()

        # Handle destination file
        if isinstance(destination, str):
            os.makedirs(os.path.dirname(os.path.abspath(destination)), exist_ok=True)
            fp = open(destination, "wb+")
            should_close = True
        else:
            fp = destination
            should_close = False

        queue = asyncio.Queue()
        for part_index in range(total_parts):
            queue.put_nowait(part_index)

        async def worker():
            nonlocal downloaded_bytes
            while not queue.empty():
                try:
                    part = queue.get_nowait()
                except asyncio.QueueEmpty:
                    break

                offset = part * chunk_size
                limit = min(chunk_size, file_size - offset)

                try:
                    r = await client.invoke(
                        raw.functions.upload.GetFile(
                            location=location,
                            offset=offset,
                            limit=limit,
                        ),
                        dc_id=dc_id,
                    )

                    if isinstance(r, raw.types.upload.File):
                        data = r.bytes
                    elif isinstance(r, raw.types.upload.FileCdnRedirect):
                        data = b""
                    else:
                        data = b""

                    async with lock:
                        fp.seek(offset)
                        fp.write(data)
                        downloaded_bytes += len(data)

                        if progress:
                            try:
                                res = progress(downloaded_bytes, file_size, *progress_args)
                                if asyncio.iscoroutine(res):
                                    await res
                            except Exception:
                                pass
                except Exception:
                    # Retry part on error
                    queue.put_nowait(part)
                    await asyncio.sleep(0.5)
                finally:
                    queue.task_done()

        worker_tasks = [asyncio.create_task(worker()) for _ in range(min(workers, total_parts))]
        await asyncio.gather(*worker_tasks)

        if should_close:
            fp.close()

        return destination

    @staticmethod
    async def parallel_upload(
        client: "ftmgram.Client",
        file_path_or_buffer: Union[str, BinaryIO, io.BytesIO],
        chunk_size: int = 1024 * 1024,  # 1 MB chunk
        workers: int = 8,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
    ) -> Union["raw.types.InputFile", "raw.types.InputFileBig"]:
        """Upload file parts concurrently across multiple workers using upload.saveBigFilePart."""
        file_id = client.rnd_id()

        if isinstance(file_path_or_buffer, str):
            file_size = os.path.getsize(file_path_or_buffer)
            file_name = os.path.basename(file_path_or_buffer)
            fp = open(file_path_or_buffer, "rb")
            should_close = True
        else:
            fp = file_path_or_buffer
            fp.seek(0, os.SEEK_END)
            file_size = fp.tell()
            fp.seek(0)
            file_name = getattr(fp, "name", "file.bin")
            should_close = False

        total_parts = math.ceil(file_size / chunk_size)
        is_big = file_size > 10 * 1024 * 1024
        uploaded_bytes = 0
        lock = asyncio.Lock()

        queue = asyncio.Queue()
        for part_index in range(total_parts):
            queue.put_nowait(part_index)

        async def worker():
            nonlocal uploaded_bytes
            while not queue.empty():
                try:
                    part = queue.get_nowait()
                except asyncio.QueueEmpty:
                    break

                offset = part * chunk_size
                async with lock:
                    fp.seek(offset)
                    chunk = fp.read(chunk_size)

                try:
                    if is_big:
                        await client.invoke(
                            raw.functions.upload.SaveBigFilePart(
                                file_id=file_id,
                                file_part=part,
                                file_total_parts=total_parts,
                                bytes=chunk,
                            )
                        )
                    else:
                        await client.invoke(
                            raw.functions.upload.SaveFilePart(
                                file_id=file_id,
                                file_part=part,
                                bytes=chunk,
                            )
                        )

                    async with lock:
                        uploaded_bytes += len(chunk)
                        if progress:
                            try:
                                res = progress(uploaded_bytes, file_size, *progress_args)
                                if asyncio.iscoroutine(res):
                                    await res
                            except Exception:
                                pass
                except Exception:
                    queue.put_nowait(part)
                    await asyncio.sleep(0.5)
                finally:
                    queue.task_done()

        worker_tasks = [asyncio.create_task(worker()) for _ in range(min(workers, total_parts))]
        await asyncio.gather(*worker_tasks)

        if should_close:
            fp.close()

        if is_big:
            return raw.types.InputFileBig(
                id=file_id,
                parts=total_parts,
                name=file_name,
            )
        else:
            return raw.types.InputFile(
                id=file_id,
                parts=total_parts,
                name=file_name,
                md5_checksum="",
            )
