Migrating to FTMGram
=====================

FTMGram is a **drop-in replacement** for both **Pyrogram** and **KuriGram**.
Migration requires a single import change — no other code modifications needed.

From Pyrogram
-------------

.. code-block:: python

   # Before
   from pyrogram import Client, filters
   from pyrogram.types import Message

   # After
   from ftmgram import Client, filters
   from ftmgram.types import Message

From KuriGram
-------------

.. code-block:: python

   # Before
   from kurigram import Client, filters
   from kurigram.types import Message

   # After
   from ftmgram import Client, filters
   from ftmgram.types import Message

Bulk Replace with sed
---------------------

Instantly update all files in your project:

.. code-block:: bash

   # From Pyrogram
   find . -name "*.py" -exec sed -i 's/from pyrogram/from ftmgram/g; s/import pyrogram/import ftmgram/g' {} +

   # From KuriGram
   find . -name "*.py" -exec sed -i 's/from kurigram/from ftmgram/g; s/import kurigram/import ftmgram/g' {} +

Compatibility Notes
-------------------

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Feature
     - Status
   * - All Pyrogram methods
     - ✅ Fully supported
   * - All Pyrogram types
     - ✅ Fully supported
   * - All Pyrogram filters
     - ✅ Fully supported
   * - Session files (``.session``)
     - ✅ Compatible — reuse existing files
   * - Custom filters
     - ✅ No changes needed
   * - Middleware / plugins
     - ✅ No changes needed
   * - Bot API 10.1 (new features)
     - ✅ Only in FTMGram

What's New vs Pyrogram
-----------------------

FTMGram adds everything Pyrogram is missing:

- **Rich Messages** — ``send_rich_message``, ``send_rich_message_draft``
- **Checklists** — ``append_checklist_tasks``, ``toggle_checklist_task``
- **Link media** — ``MessageMediaType.LINK``, ``Link`` type
- **Join-request queries** — ``answer_chat_join_request_query``
- **Star balance** — ``get_owned_star_count``

See :doc:`../changelog` for the full list.
