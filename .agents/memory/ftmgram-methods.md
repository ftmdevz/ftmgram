---
name: ftmgram method registration
description: How new methods are added to ftmgram and pre-existing import bugs fixed
---

# Rules for adding new methods to ftmgram

1. Create `ftmgram/methods/<category>/<method_name>.py` with a class matching `ClassName`
2. Add `from .<method_name> import ClassName` to `ftmgram/methods/<category>/__init__.py`
3. Add `ClassName` to the mixin class in that same `__init__.py`

# Pre-existing typing import bugs

Many pre-existing files in `ftmgram/methods/` used `Union`, `List`, `Optional`, etc. without importing them from `typing`. Two flavors:
- Files with `from typing import X` but missing some names → extend the import line
- Files with NO `from typing import` at all → insert one after the license header

**Fix script:** use regex to scan for usage of typing names vs. what's imported, then patch each file.

# Methods added in this session

**Messages:** forward_message, delete_message, copy_messages
**Chats:** ban_chat_sender_chat, unban_chat_sender_chat, set_chat_sticker_set, delete_chat_sticker_set, unpin_all_forum_topic_messages, create_chat_subscription_invite_link
**Stickers:** get_sticker_set, upload_sticker_file, create_new_sticker_set, add_sticker_to_set, set_sticker_position_in_set, delete_sticker_from_set, set_sticker_set_title, set_sticker_set_thumbnail, set_custom_emoji_sticker_set_thumbnail, set_sticker_emoji_list, set_sticker_keywords, set_sticker_mask_position, delete_sticker_set
**Users:** get_user_profile_photos, get_user_chat_boosts
**Payments:** get_star_transactions, pin_gift, unpin_gift, get_owned_gifts
**Business:** read_business_message
**Account:** set_business_account_bio (in account/ folder)
**Bots:** set_passport_data_errors
**Utilities:** get_file

# Also fixed

- edit_inline_caption.py, edit_message_checklist.py, send_checklist.py, translate_message_text.py: missing List/Union
- 50+ pre-existing files: missing typing imports (automated fix via regex script)
