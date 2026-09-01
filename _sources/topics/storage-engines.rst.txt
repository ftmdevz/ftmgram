Storage Engines
===============

FTMGram supports three distinct session storage mechanisms:

1. File-Based SQLite Storage
----------------------------
Default storage engine. Persists session state (authorization keys, peers cache) in a local ``<name>.session`` file.

.. code-block:: python

   from ftmgram import Client

   app = Client("my_account")

2. In-Memory Temporary Storage
------------------------------
Session data is kept strictly in RAM and discarded when the process terminates.

.. code-block:: python

   app = Client("temp_session", in_memory=True)

3. Session Strings
------------------
A base64 string session containing the authorization key, ideal for serverless cloud environments (Heroku, Render, AWS Lambda).

.. code-block:: python

   # Generate session string
   async with Client("my_session") as app:
       string = await app.export_session_string()
       print(string)

   # Load from session string
   app = Client("cloud_app", session_string=string)
