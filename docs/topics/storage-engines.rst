Storage Engines
===============

FTMGram supports three session storage mechanisms:

1. File-Based SQLite Sessions
-----------------------------

.. code-block:: python

   from ftmgram import Client
   app = Client("my_account")

2. In-Memory Temporary Sessions
-------------------------------

.. code-block:: python

   app = Client("temp_bot", in_memory=True)

3. Session Strings
------------------

.. code-block:: python

   async with Client("my_session") as app:
       string = await app.export_session_string()
       print(string)
