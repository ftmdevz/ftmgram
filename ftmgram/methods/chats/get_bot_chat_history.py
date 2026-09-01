import asyncio
from typing import AsyncGenerator, Optional, Union, List
import ftmgram
from ftmgram import types


class GetBotChatHistory:
    async def get_bot_chat_history(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        start_message_id: int = 1,
        limit: int = 100,
        reverse: bool = False,
        chunk_size: int = 100,
    ) -> AsyncGenerator["types.Message", None]:
        """Fetch message history for bots in private chats and groups by batch scanning message IDs.

        This method works around Telegram's bot limitation on `messages.getHistory` by querying
        batches of up to 100 message IDs concurrently using `get_messages()`. It skips non-existent
        or deleted messages and yields only valid Message objects.

        Example:
            .. code-block:: python

                async for message in app.get_bot_chat_history(chat_id=123456789, start_message_id=1, limit=50):
                    print(f"[{message.id}] {message.text}")

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int or username) of the target chat.

            start_message_id (``int``, *optional*):
                The message ID to begin scanning from. Defaults to 1.

            limit (``int``, *optional*):
                Maximum number of valid messages to yield. Defaults to 100.

            reverse (``bool``, *optional*):
                If True, scans downwards (decreasing IDs) from `start_message_id`. Defaults to False (scans upwards).

            chunk_size (``int``, *optional*):
                Number of message IDs to request in a single RPC batch (max 100). Defaults to 100.

        Yields:
            :obj:`~ftmgram.types.Message`: Valid message objects in the requested range.
        """
        current_id = max(1, start_message_id)
        chunk_size = min(100, max(1, chunk_size))
        yielded_count = 0

        while yielded_count < limit:
            if reverse:
                end_id = max(1, current_id - chunk_size + 1)
                batch_ids = list(range(current_id, end_id - 1, -1))
                current_id = end_id - 1
                if not batch_ids:
                    break
            else:
                end_id = current_id + chunk_size
                batch_ids = list(range(current_id, end_id))
                current_id = end_id

            try:
                messages: List[Optional["types.Message"]] = await self.get_messages(chat_id, batch_ids)
            except Exception:
                await asyncio.sleep(0.5)
                continue

            if not messages:
                if reverse and current_id <= 1:
                    break
                continue

            found_any = False
            for msg in messages:
                if msg is not None and getattr(msg, "id", None) is not None:
                    found_any = True
                    yield msg
                    yielded_count += 1
                    if yielded_count >= limit:
                        return

            if reverse and current_id <= 1:
                break

            await asyncio.sleep(0.05)
