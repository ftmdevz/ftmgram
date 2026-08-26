<p align="center">
    <a href="https://github.com/ftmdevz/ftmgram">
        <img src="https://raw.githubusercontent.com/ftmdevz/ftmgram/master/logo.png" alt="FTMGram" width="160">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br><br>
    <a href="https://pypi.python.org/pypi/ftmgram">
        <img src="https://img.shields.io/pypi/v/ftmgram.svg?logo=pypi&logoColor=white&color=orange" alt="PyPI version">
    </a>
    <a href="https://pypi.python.org/pypi/ftmgram">
        <img src="https://img.shields.io/pypi/l/ftmgram.svg?color=orange" alt="License">
    </a>
    <a href="https://pypi.python.org/pypi/ftmgram">
        <img src="https://img.shields.io/pypi/pyversions/ftmgram.svg?logo=python&logoColor=white" alt="Python versions">
    </a>
    <a href="https://github.com/ftmdevz/ftmgram">
        <img src="https://img.shields.io/github/stars/ftmdevz/ftmgram?style=flat&color=orange" alt="GitHub Stars">
    </a>
</p>

---

## FTMGram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python — for users and bots

**FTMGram** is an actively maintained, feature-complete fork of Pyrogram with full **Bot API 10.1** (June 2026) support. It is a drop-in replacement for Pyrogram and KuriGram with zero migration friction.

```python
from ftmgram import Client, filters

app = Client("my_account")

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from FTMGram!")

app.run()
```

---

### What's New in v3.3.0 — Bot API 10.1

| Feature | Status |
|---|---|
| **Rich Messages** — `sendRichMessage`, `sendRichMessageDraft`, `editMessageText` | ✅ |
| **RichText** — 14 inline text types (Bold, Italic, Url, Code, Marked, …) | ✅ |
| **RichBlock** — 19 block types (Paragraph, Photo, Video, Table, Slideshow, …) | ✅ |
| **Checklist media** — `MessageMediaType.CHECKLIST`, `Checklist`, `ChecklistTask` | ✅ |
| **Link poll media** — `MessageMediaType.LINK`, `Link` type | ✅ |
| **Chat join request queries** — `answerChatJoinRequestQuery`, `sendChatJoinRequestWebApp` | ✅ |
| `User.supports_join_request_queries`, `Chat.guard_bot`, `ChatJoinRequest.query_id` | ✅ |
| **Owned star balance** — `get_owned_star_count` | ✅ |

---

### Key Features

- **Ready** — `pip install ftmgram` and start building immediately.
- **Easy** — Clean, Pythonic API that hides MTProto complexity.
- **Elegant** — Low-level details abstracted into intuitive high-level types.
- **Fast** — Powered by [TgCrypto](https://github.com/pyrogram/tgcrypto), a C-level cryptography library.
- **Type-hinted** — Full type annotations for excellent IDE/editor support.
- **Async** — Fully asynchronous; synchronous usage also supported.
- **Powerful** — Complete access to Telegram's API — every official client action and more.
- **Bot API 10.1 complete** — Latest Telegram features covered on day one.

---

### Installing

**Stable (PyPI)**

```bash
pip install ftmgram
```

**Latest (GitHub)**

```bash
pip install https://github.com/ftmdevz/ftmgram/archive/ftmdevz.zip --force-reinstall
```

---

### Quick Example — Rich Message

```python
from ftmgram import Client
from ftmgram.types import InputRichMessage, InputRichMessageContent, RichText

app = Client("my_bot", bot_token="TOKEN")

async def main():
    await app.send_rich_message(
        chat_id=123456,
        rich_message=InputRichMessage(
            title=RichText.plain("FTMGram Guide"),
            content=[
                InputRichMessageContent.paragraph(
                    text=RichText.concat([
                        RichText.bold("FTMGram"),
                        RichText.plain(" supports full Bot API 10.1!"),
                    ])
                )
            ]
        )
    )

app.run(main())
```

---

### Support

FTMGram is open source. Support its development:

- [contact me on telegram for donation by clicking here](https://t.me/ftmdevz)

Thank you ❤️

---

### Resources

- [GitHub Repository](https://github.com/ftmdevz/ftmgram)
- [PyPI Package](https://pypi.org/project/ftmgram/)
- [Telegram Channel](https://t.me/ftmdeveloperz) — news & updates
- [Telegram Chat](https://t.me/ftmdevz) — community support

---

<p align="center">
    <sub>FTMGram is a fork of <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a> and <a href="https://github.com/ftmdevz/ftmgram">FTMGram</a>. Licensed under LGPLv3.</sub>
</p>
