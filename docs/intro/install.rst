Installation
============

Requirements
------------

- **Python 3.8** or higher
- **pip** (bundled with Python)

Stable Release — PyPI
---------------------

Install the latest stable release from PyPI:

.. code-block:: bash

   pip install ftmgram

Install with optional speed extras (TgCrypto C-extension + uvloop):

.. code-block:: bash

   pip install "ftmgram[fast]"

.. note::

   ``tgcrypto`` significantly speeds up encryption/decryption. It is highly
   recommended for production bots and user clients.

Latest from GitHub
------------------

Install directly from the ``ftmdevz`` development branch:

.. code-block:: bash

   pip install https://github.com/ftmdevz/ftmgram/archive/ftmdevz.zip --force-reinstall

Verify Installation
-------------------

.. code-block:: python

   import ftmgram
   print(ftmgram.__version__)  # 3.0.0

Optional Dependencies
---------------------

.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Extra
     - Package
     - Description
   * - ``fast``
     - ``tgcrypto``
     - C-level AES/IGE crypto — much faster than pure Python
   * - ``fast``
     - ``uvloop``
     - High-performance asyncio event loop (Linux/macOS only)

Upgrading
---------

.. code-block:: bash

   pip install -U ftmgram
