from typing import List, Optional, Union
from ftmgram.types import (
    InputRichMessage,
    InputRichBlockButtons,
    RichMessageButton,
    InputRichBlockParagraph,
    InputRichBlockTable,
    InputRichBlockExpandableBlockQuotation,
)


class Button:
    """Represents a button in a Rich Message layout.

    Parameters:
        text (``str``):
            The text to display on the button.

        data (``str``, *optional*):
            Callback data for callback buttons.

        url (``str``, *optional*):
            URL for link buttons.

        style (``str``, *optional*):
            Style of button: "primary", "secondary", "success", "danger". Defaults to "primary".
    """

    def __init__(
        self,
        text: str,
        data: Optional[str] = None,
        url: Optional[str] = None,
        style: str = "primary",
    ):
        self.text = text
        self.data = data
        self.url = url
        self.style = style

    def to_rich_button(self) -> RichMessageButton:
        return RichMessageButton(
            text=self.text,
            callback_data=self.data,
            url=self.url,
            style=self.style,
        )


class RichMessageBuilder:
    """Fluent Builder DSL for constructing Telegram Bot API 10.3 Rich Messages.

    Example:
        .. code-block:: python

            from ftmgram.helpers import RichMessageBuilder, Button

            rich = (
                RichMessageBuilder()
                .title("🚀 FTMGram v3.4.0")
                .paragraph("Explore next-gen MTProto features:")
                .button_row(
                    Button("Documentation", url="https://ftmgram.ftmbotzx.dev", style="primary"),
                    Button("Join Channel", url="https://t.me/ftmdeveloperz", style="success")
                )
                .build()
            )
            await app.send_rich_message(chat_id, rich)
    """

    def __init__(self):
        self.html_parts: List[str] = []
        self.button_rows: List[List[RichMessageButton]] = []

    def title(self, text: str) -> "RichMessageBuilder":
        """Add a bold header title."""
        self.html_parts.append(f"<b>{text}</b>\n")
        return self

    def paragraph(self, text: str) -> "RichMessageBuilder":
        """Add a paragraph of text."""
        self.html_parts.append(f"{text}\n")
        return self

    def quote(self, text: str, expandable: bool = False) -> "RichMessageBuilder":
        """Add a blockquote or expandable quote."""
        if expandable:
            self.html_parts.append(f"<blockquote expandable>{text}</blockquote>\n")
        else:
            self.html_parts.append(f"<blockquote>{text}</blockquote>\n")
        return self

    def code(self, code: str, language: str = "") -> "RichMessageBuilder":
        """Add a formatted code block."""
        if language:
            self.html_parts.append(f'<pre><code class="language-{language}">{code}</code></pre>\n')
        else:
            self.html_parts.append(f"<pre>{code}</pre>\n")
        return self

    def button_row(self, *buttons: Union[Button, RichMessageButton]) -> "RichMessageBuilder":
        """Add a horizontal row of in-message styled buttons."""
        row_html = ['<tg-button-row align="center">']
        for btn in buttons:
            if isinstance(btn, Button):
                if btn.url:
                    row_html.append(f'<tg-button type="url" style="{btn.style}" url="{btn.url}">{btn.text}</tg-button>')
                else:
                    row_html.append(f'<tg-button type="callback_data" style="{btn.style}" data="{btn.data or ""}">{btn.text}</tg-button>')
            elif isinstance(btn, RichMessageButton):
                if btn.url:
                    row_html.append(f'<tg-button type="url" style="{btn.style or "primary"}" url="{btn.url}">{btn.text}</tg-button>')
                else:
                    row_html.append(f'<tg-button type="callback_data" style="{btn.style or "primary"}" data="{btn.callback_data or ""}">{btn.text}</tg-button>')
        row_html.append("</tg-button-row>\n")
        self.html_parts.append("".join(row_html))
        return self

    def build(self) -> InputRichMessage:
        """Compile into an InputRichMessage ready to send."""
        full_html = "".join(self.html_parts).strip()
        return InputRichMessage(html=full_html)
