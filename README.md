<div align="center">
  <img src="https://raw.githubusercontent.com/ftmdevz/ftmgram/ftmdevz/docs/static/img/ftmgram_icon.svg" width="100" height="100" alt="FTMGram Logo" />
  <h1>FTMGram v3.5.1</h1>
  <p><b>Next-Gen Telegram MTProto & Bot API 10.3 Framework for Python</b></p>
  <p>
    <a href="https://ftmgram.ftmbotzx.dev"><img src="https://img.shields.io/badge/docs-ftmgram.ftmbotzx.dev-orange?style=flat-square" alt="Docs"></a>
    <a href="https://pypi.org/project/ftmgram/"><img src="https://img.shields.io/pypi/v/ftmgram.svg?style=flat-square" alt="PyPI"></a>
    <a href="https://t.me/ftmdeveloperz"><img src="https://img.shields.io/badge/telegram-channel-blue?style=flat-square&logo=telegram" alt="Telegram"></a>
    <a href="https://github.com/ftmdevz/ftmgram/blob/ftmdevz/LICENSE"><img src="https://img.shields.io/badge/license-LGPL--3.0-green?style=flat-square" alt="License"></a>
  </p>
</div>

---

**FTMGram** is a rock-solid, high-performance, asynchronous Telegram MTProto client library and Bot API framework for Python. It supercharges both user accounts and bots with modern features like **Turbo Multi-Worker Transfers (Upload & Download)**, **In-Message Buttons**, **AI Response Token Streaming**, **Bot Chat History Scanning**, and **Telegram Stars 2.0**.

---

## ⚡ Key Highlights in v3.5.1

* **🛡️ 100% Rock-Solid Stability**:
  Zero file descriptor leaks on Linux / `uvloop` containers (`[Errno 24] Too many open files` completely eliminated).
* **⚡ Turbo Multi-Worker Upload Engine (`fast_upload`)**:
  Upload videos, documents, and large files up to 2GB/4GB at maximum speed using concurrent multi-worker chunk streaming.
* **⚡ Turbo Multi-Worker Download Engine (`fast_download`)**:
  Download media files concurrently with parallel chunk workers for gigabit saturation.
* **🤖 Bot Chat History (`get_bot_chat_history`)**:
  Allows bots to retrieve message history across private chats and groups using safe, high-speed 100-ID batch scanning.
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

### 1. Fast Upload & Fast Download (Turbo Transfers)

```python
from ftmgram import Client

app = Client("my_bot", bot_token="TOKEN")

async def upload_and_download():
    async with app:
        # Fast Upload with 8 parallel workers
        uploaded_file = await app.fast_upload("large_video.mp4", workers=8)
        msg = await app.send_video(123456789, video=uploaded_file, caption="Sent via Turbo Upload! 🚀")

        # Fast Download with 8 parallel workers
        await app.fast_download(msg, file_name="downloads/", workers=8)

app.run(upload_and_download())
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

### 3. Bot Chat History Retrieval

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
* **[Releases & Changelog](https://ftmgram.ftmbotzx.dev/releases/index.html)**

---

## 📜 License

FTMGram is licensed under the **GNU Lesser General Public License v3.0 (LGPL-3.0)**.
Copyright (C) 2024-present [FTM DEVELOPERZ](https://github.com/ftmdevz).
