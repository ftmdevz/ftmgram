Checklists & Task Lists
=======================

Send interactive task lists where users can check off completed items in real-time.

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import Checklist, ChecklistTask

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           await app.send_checklist(
               chat_id=123456789,
               title="Tasks",
               tasks=[
                   ChecklistTask(id=1, text="Deploy FTMGram Docs", is_completed=True),
                   ChecklistTask(id=2, text="Test Bot API 10.3", is_completed=True),
               ]
           )

   app.run(main())
