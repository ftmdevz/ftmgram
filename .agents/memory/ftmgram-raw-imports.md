---
name: ftmgram raw import fix
description: All generated files in ftmgram/raw/ imported from pyrogram instead of ftmgram — must stay as ftmgram.
---

All 8600+ files under `ftmgram/raw/` (base/, types/, functions/) were generated with `from pyrogram import raw` and `from pyrogram.raw.core import BaseTypeMeta`. These must be `from ftmgram import raw` and `from ftmgram.raw.core import BaseTypeMeta`.

**Why:** ftmgram is a fork with its own extended raw TL schema (newer types like UpdateJoinChatWebViewDecision, MessageMediaToDo, etc. that don't exist in pyrogram). Using pyrogram.raw causes AttributeError at import time.

**How to apply:** If the raw module is ever regenerated (e.g. via `compiler/` scripts), run the bulk fix immediately after:
```
find ftmgram/raw -name "*.py" | xargs sed -i 's/from pyrogram import raw/from ftmgram import raw/g; s/from pyrogram\.raw\.core import/from ftmgram.raw.core import/g; s/from pyrogram\.raw import/from ftmgram.raw import/g'
```
