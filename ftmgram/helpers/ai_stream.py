import asyncio
import io
import time
from contextlib import asynccontextmanager
from typing import AsyncIterable, Optional, Union

import ftmgram
from ftmgram.types import InputRichMessage


async def stream_text(
    client: "ftmgram.Client",
    chat_id: Union[int, str],
    stream: AsyncIterable[str],
    chunk_interval: float = 0.15,
    placeholder: str = "Thinking...",
    can_stop: bool = True,
    reply_to_message_id: Optional[int] = None,
) -> Optional["ftmgram.types.Message"]:
    """Stream text tokens in real-time to a Telegram chat using native drafts.

    Parameters:
        client (:obj:`~ftmgram.Client`):
            The FTMGram client instance.

        chat_id (``int`` | ``str``):
            Unique identifier (int or username) of the target chat.

        stream (``AsyncIterable[str]``):
            An async iterator yielding text chunks (e.g. from OpenAI, Gemini, Groq, Ollama).

        chunk_interval (``float``, *optional*):
            Minimum interval between draft updates in seconds to avoid rate limits. Defaults to 0.15.

        placeholder (``str``, *optional*):
            Initial thinking placeholder text. Defaults to "Thinking...".

        can_stop (``bool``, *optional*):
            Whether to allow users to cancel the streaming process. Defaults to True.

        reply_to_message_id (``int``, *optional*):
            If the final message should reply to a specific message ID.

    Returns:
        :obj:`~ftmgram.types.Message`: The finalized sent message object.
    """
    draft_id = client.rnd_id()

    # Send initial thinking placeholder
    if placeholder:
        try:
            await client.send_rich_message_draft(
                chat_id=chat_id,
                draft_id=draft_id,
                rich_message=InputRichMessage(html=f"<tg-thinking>{placeholder}</tg-thinking>"),
                can_stop=can_stop,
            )
        except Exception:
            pass

    accumulated = ""
    last_update = time.time()

    async for chunk in stream:
        accumulated += chunk
        now = time.time()
        if now - last_update >= chunk_interval:
            last_update = now
            try:
                await client.send_rich_message_draft(
                    chat_id=chat_id,
                    draft_id=draft_id,
                    rich_message=InputRichMessage(markdown=accumulated),
                    can_stop=can_stop,
                )
            except Exception:
                pass

    # Send final complete message
    return await client.send_message(
        chat_id=chat_id,
        text=accumulated,
        reply_to_message_id=reply_to_message_id,
    )


@asynccontextmanager
async def thinking(
    client: "ftmgram.Client",
    chat_id: Union[int, str],
    text: str = "Thinking...",
    can_stop: bool = True,
):
    """Context manager for displaying an animated native thinking state while performing background tasks.

    Example:
        .. code-block:: python

            async with app.thinking(chat_id, text="Searching knowledge base..."):
                results = await fetch_data()
            await app.send_message(chat_id, f"Found: {results}")

    Parameters:
        client (:obj:`~ftmgram.Client`):
            The FTMGram client instance.

        chat_id (``int`` | ``str``):
            Unique identifier of the target chat.

        text (``str``, *optional*):
            Placeholder text to display. Defaults to "Thinking...".

        can_stop (``bool``, *optional*):
            Whether to show the Stop button. Defaults to True.
    """
    draft_id = client.rnd_id()
    try:
        await client.send_rich_message_draft(
            chat_id=chat_id,
            draft_id=draft_id,
            rich_message=InputRichMessage(html=f"<tg-thinking>{text}</tg-thinking>"),
            can_stop=can_stop,
        )
    except Exception:
        pass

    try:
        yield draft_id
    finally:
        pass
