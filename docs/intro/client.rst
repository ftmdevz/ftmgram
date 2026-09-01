Client Configuration
====================

The ``Client`` class is the central orchestrator for interacting with Telegram MTProto.

Constructor Parameters
----------------------

.. list-table::
   :widths: 25 20 55
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - ``name``
     - ``str``
     - Session identifier (stores ``name.session`` SQLite file).
   * - ``api_id``
     - ``int``
     - Telegram API ID from `my.telegram.org <https://my.telegram.org>`_.
   * - ``api_hash``
     - ``str``
     - Telegram API Hash from `my.telegram.org <https://my.telegram.org>`_.
   * - ``bot_token``
     - ``str``
     - Bot Token from ``@BotFather`` (leave None for user accounts).
   * - ``session_string``
     - ``str``
     - In-memory string session for serverless deployments.
   * - ``in_memory``
     - ``bool``
     - If True, session is stored entirely in memory (no disk file created).
   * - ``workdir``
     - ``str``
     - Working directory for session files.
   * - ``proxy``
     - ``dict``
     - SOCKS5 / SOCKS4 / HTTP proxy dictionary.

Example
-------

.. code-block:: python

   from ftmgram import Client

   # Standard Bot Session
   app = Client(
       "my_bot",
       api_id=12345,
       api_hash="0123456789abcdef0123456789abcdef",
       bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
   )
