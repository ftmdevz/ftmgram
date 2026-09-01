import io
from typing import Optional, Union
import ftmgram


class DownloadMediaToMemory:
    async def download_media_to_memory(
        self: "ftmgram.Client",
        message: Union["ftmgram.types.Message", str],
        progress: Optional[callable] = None,
        progress_args: tuple = (),
    ) -> Optional[io.BytesIO]:
        """Download a media file directly into an in-memory BytesIO buffer.

        Parameters:
            message (:obj:`~ftmgram.types.Message` | ``str``):
                Pass a Message object containing media or a file_id string.

            progress (``Callable``, *optional*):
                Pass a callback function to view the progress.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback.

        Returns:
            :obj:`io.BytesIO` | ``None``: The BytesIO buffer holding downloaded binary data.
        """
        buffer = io.BytesIO()
        await self.download_media(
            message=message,
            file_name=buffer,
            progress=progress,
            progress_args=progress_args,
        )
        buffer.seek(0)
        return buffer
