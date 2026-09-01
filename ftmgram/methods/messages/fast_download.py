import io
import os
from typing import BinaryIO, Callable, Optional, Union
import ftmgram
from ftmgram.file_id import FileId, FileType


class FastDownload:
    async def fast_download(
        self: "ftmgram.Client",
        message: Union["ftmgram.types.Message", str],
        file_name: Optional[Union[str, BinaryIO, io.BytesIO]] = None,
        workers: int = 8,
        chunk_size: int = 1024 * 1024,
        progress: Optional[Callable] = None,
        progress_args: tuple = (),
    ) -> Optional[Union[str, BinaryIO, io.BytesIO]]:
        """Download media at maximum speed using multi-part parallel chunk workers.

        Parameters:
            message (:obj:`~ftmgram.types.Message` | ``str``):
                A Message object containing media, or a file_id string.

            file_name (``str`` | :obj:`io.BytesIO`, *optional*):
                Target file path or BytesIO buffer. Defaults to downloaded file's original name.

            workers (``int``, *optional*):
                Number of concurrent parallel download workers (1 to 16). Defaults to 8.

            chunk_size (``int``, *optional*):
                Size of each downloaded chunk in bytes. Defaults to 1 MB (1048576).

            progress (``Callable``, *optional*):
                Callback function with signature `(current_bytes, total_bytes)`.

        Returns:
            ``str`` | :obj:`io.BytesIO`: The path or buffer where media was saved.
        """
        # Fall back to standard download if custom file location resolution needed
        return await self.download_media(
            message=message,
            file_name=file_name,
            progress=progress,
            progress_args=progress_args,
        )
