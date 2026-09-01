import io
import os
from typing import BinaryIO, Callable, Optional, Union
import ftmgram
from ftmgram import raw
from ftmgram.helpers.turbo_transfer import TurboTransfer


class FastUpload:
    async def fast_upload(
        self: "ftmgram.Client",
        file: Union[str, BinaryIO, io.BytesIO],
        workers: int = 8,
        chunk_size: int = 1024 * 1024,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
    ) -> Union["raw.types.InputFile", "raw.types.InputFileBig"]:
        """Upload a file or buffer at maximum speed using multi-part parallel chunk workers.

        Parameters:
            file (``str`` | :obj:`io.BytesIO` | ``BinaryIO``):
                The path to the file to upload, or an in-memory binary stream.

            workers (``int``, *optional*):
                Number of concurrent parallel upload workers (1 to 16). Defaults to 8.

            chunk_size (``int``, *optional*):
                Size of each uploaded chunk in bytes. Defaults to 1 MB (1048576).

            progress (``Callable``, *optional*):
                Callback function with signature `(current_bytes, total_bytes)`.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback.

        Returns:
            :obj:`~ftmgram.raw.types.InputFile` | :obj:`~ftmgram.raw.types.InputFileBig`: The uploaded MTProto input file object ready to be passed to send_video, send_document, etc.
        """
        return await TurboTransfer.parallel_upload(
            client=self,
            file_path_or_buffer=file,
            chunk_size=chunk_size,
            workers=workers,
            progress=progress,
            progress_args=progress_args,
        )
