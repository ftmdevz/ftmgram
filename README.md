<div align="center">
  <img src="https://raw.githubusercontent.com/ftmdevz/ftmgram/ftmdevz/docs/static/img/ftmgram_icon.svg" width="100" height="100" alt="FTMGram Logo" />
  <h1>FTMGram v3.5.0</h1>
  <p><b>Next-Gen Telegram MTProto & Bot API 10.3 Framework for Python</b></p>
  <p>
    <a href="https://ftmgram.ftmbotzx.dev"><img src="https://img.shields.io/badge/docs-ftmgram.ftmbotzx.dev-orange?style=flat-square" alt="Docs"></a>
    <a href="https://pypi.org/project/ftmgram/"><img src="https://img.shields.io/pypi/v/ftmgram.svg?style=flat-square" alt="PyPI"></a>
    <a href="https://t.me/ftmdeveloperz"><img src="https://img.shields.io/badge/telegram-channel-blue?style=flat-square&logo=telegram" alt="Telegram"></a>
    <a href="https://github.com/ftmdevz/ftmgram/blob/ftmdevz/LICENSE"><img src="https://img.shields.io/badge/license-LGPL--3.0-green?style=flat-square" alt="License"></a>
  </p>
</div>

---

**FTMGram** is a high-performance, asynchronous Telegram MTProto client library and Bot API framework for Python. It supercharges both user accounts and bots with modern features like **In-Message Buttons**, **AI Response Token Streaming**, **Bot Chat History Scanning**, **Turbo Multi-Worker Transfers**, **Ephemeral Overlays**, and **Telegram Stars 2.0**.

---

## ⚡ Key Highlights in v3.5.0

* **🤖 Bot Chat History (`get_bot_chat_history`)**:
  Allows bots to retrieve message history across private chats and groups using safe, high-speed 100-ID batch scanning.
* **⚡ Turbo Multi-Worker Media Engine (`fast_download`)**:
  Download photos, videos, and large files at maximum network saturation with parallel chunk workers.
* **🎨 Fluent `RichMessageBuilder` DSL**:
  Construct structured rich messages with in-message buttons (`<tg-button-row>`), expandable quotes, tables, and paragraphs effortlessly in Python.
* **🧠 Real-Time AI Streaming (`stream_text` & `thinking`)**:
  Seamlessly stream LLM tokens (OpenAI, Anthropic, Gemini, Groq, Ollama) directly to chat drafts with animated thinking placeholders and stop buttons.
* **🧹 Batch Chat Purge (`purge_messages`)**:
  Safely delete hundreds of messages in seconds with automatic RPC chunking and rate-limit handling.
* **💾 Memory Media Streaming (`download_media_to_memory`)**:
  Download media straight into an in-memory `io.BytesIO` buffer without disk I/O bottlenecks.
* **👥 Multi-Client Orchestrator (`MultiClient`)**:
  Manage and run dozens of bots and user accounts concurrently in a single event loop.

---

## 📦 Installation

```bash
pip install -U ftmgram
```

Or install with fast cryptographic acceleration:

```bash
pip install -U "ftmgram[fast]"
```

---

## 🚀 Quick Examples

### 1. Echo Bot with Filters

```python
from ftmgram import Client, filters

app = Client("my_bot", bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(f"You said: {message.text}")

app.run()
```

---

### 2. In-Message Buttons (Bot API 10.3)

```python
from ftmgram import Client
from ftmgram.helpers import RichMessageBuilder, Button

app = Client("my_bot", bot_token="TOKEN")

async def send_menu(chat_id: int):
    async with app:
        rich = (
            RichMessageBuilder()
            .title("💎 VIP Subscription")
            .paragraph("Select your desired membership tier:")
            .button_row(
                Button("Starter ($5)", data="plan_starter", style="primary"),
                Button("Pro ($15)", data="plan_pro", style="success"),
                Button("VIP ($25)", data="plan_vip", style="danger")
            )
            .build()
        )
        await app.send_rich_message(chat_id, rich)

app.run(send_menu(123456789))
```

---

### 3. Real-Time AI Token Streaming

```python
from ftmgram import Client

app = Client("my_bot", bot_token="TOKEN")

async def fake_ai_stream():
    for word in ["Generating ", "answers ", "with ", "FTMGram ", "v3.5.0! 🚀"]:
        yield word

async def main():
    async with app:
        await app.stream_text(
            chat_id=123456789,
            stream=fake_ai_stream(),
            placeholder="AI is reasoning..."
        )

app.run(main())
```

---

### 4. Bot Chat History Retrieval

```python
from ftmgram import Client

app = Client("my_bot", bot_token="TOKEN")

async def scan_history(chat_id: int):
    async with app:
        async for msg in app.get_bot_chat_history(chat_id, start_message_id=1, limit=50):
            print(f"[{msg.id}] {msg.text}")

app.run(scan_history(123456789))
```

---

## 📚 Documentation

Visit the official documentation portal: **[https://ftmgram.ftmbotzx.dev/](https://ftmgram.ftmbotzx.dev/)**

* **[Getting Started](https://ftmgram.ftmbotzx.dev/intro/quickstart.html)**
* **[Methods Index](https://ftmgram.ftmbotzx.dev/api/methods/index.html)**
* **[Types Reference](https://ftmgram.ftmbotzx.dev/api/types/index.html)**
* **[Bot API 10.3 Topics](https://ftmgram.ftmbotzx.dev/topics/rich-messages.html)**

---

## 📜 License

FTMGram is licensed under the **GNU Lesser General Public License v3.0 (LGPL-3.0)**.
Copyright (C) 2024-present [FTM DEVELOPERZ](https://github.com/ftmdevz).
