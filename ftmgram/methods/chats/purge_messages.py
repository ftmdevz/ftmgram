import asyncio
from typing import List, Optional, Union
import ftmgram


class PurgeMessages:
    async def purge_messages(
        self: "ftmgram.Client",
        chat_id: Union[int, str],
        limit: int = 100,
        from_message_id: Optional[int] = None,
        to_message_id: Optional[int] = None,
        from_user: Optional[Union[int, str]] = None,
    ) -> int:
        """Purge and bulk delete messages in a chat safely with rate-limit protection.

        Parameters:
            chat_id (``int`` | ``str``):
                Target chat ID or username.

            limit (``int``, *optional*):
                Maximum number of messages to delete. Defaults to 100.

            from_message_id (``int``, *optional*):
                Starting message ID range.

            to_message_id (``int``, *optional*):
                Ending message ID range.

            from_user (``int`` | ``str``, *optional*):
                Filter messages from a specific user only.

        Returns:
            ``int``: The total count of deleted messages.
        """
        deleted_count = 0
        message_ids: List[int] = []

        async for message in self.get_chat_history(chat_id, limit=limit):
            if from_message_id and message.id < from_message_id:
                continue
            if to_message_id and message.id > to_message_id:
                continue
            if from_user:
                if not message.from_user:
                    continue
                if isinstance(from_user, int) and message.from_user.id != from_user:
                    continue
                if isinstance(from_user, str) and message.from_user.username != from_user.lstrip("@"):
                    continue

            message_ids.append(message.id)

            if len(message_ids) >= 100:
                await self.delete_messages(chat_id, message_ids)
                deleted_count += len(message_ids)
                message_ids.clear()
                await asyncio.sleep(0.5)

        if message_ids:
            await self.delete_messages(chat_id, message_ids)
            deleted_count += len(message_ids)

        return deleted_count
