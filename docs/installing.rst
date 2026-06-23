Installing
==========

Requirements
------------

- Python **3.8** or higher
- pip (comes with Python)

Stable Release (PyPI)
---------------------

Install the latest stable version from PyPI:

.. code-block:: bash

   pip install ftmgram

With optional speed extras (TgCrypto + uvloop):

.. code-block:: bash

   pip install "ftmgram[fast]"

Latest from GitHub
------------------

Install the latest ``master`` branch directly:

.. code-block:: bash

   pip install https://github.com/ftmdevz/ftmgram/archive/master.zip --force-reinstall

Development branch:

.. code-block:: bash

   pip install https://github.com/ftmdevz/ftmgram/archive/dev.zip --force-reinstall

Verify Installation
-------------------

.. code-block:: python

   import ftmgram
   print(ftmgram.__version__)  # 3.0.0

Migrating from Pyrogram / KuriGram
-----------------------------------

FTMGram is a **drop-in replacement**. Just change the import:

.. code-block:: python

   # Before
   from pyrogram import Client
   # or
   from kurigram import Client

   # After
   from ftmgram import Client

No other code changes needed.
