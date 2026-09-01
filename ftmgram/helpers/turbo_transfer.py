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
                except Exception as e:
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
