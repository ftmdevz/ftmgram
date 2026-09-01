Checklists
==========

Checklists are interactive task list messages introduced in **Bot API 10.1**.
Users can check and uncheck tasks directly in the chat.

Sending a Checklist
-------------------

.. code-block:: python

   from ftmgram import Client
   from ftmgram.types import InputChecklistTask

   app = Client("my_bot", bot_token="TOKEN")

   async def main():
       async with app:
           msg = await app.send_message(
               chat_id=123456789,
               text="My shopping list",
               checklist=[
                   InputChecklistTask(text="Milk"),
                   InputChecklistTask(text="Eggs"),
                   InputChecklistTask(text="Bread", completed=True),
               ]
           )

   app.run(main())

Adding Tasks to an Existing Checklist
--------------------------------------

.. code-block:: python

   await app.append_checklist_tasks(
       chat_id=123456789,
       message_id=msg.id,
       tasks=[
           InputChecklistTask(text="Butter"),
           InputChecklistTask(text="Cheese"),
       ]
   )

Checking / Unchecking a Task
-----------------------------

.. code-block:: python

   await app.toggle_checklist_task(
       chat_id=123456789,
       message_id=msg.id,
       task_id=task.id,
       completed=True
   )

Reading a Checklist
--------------------

When a message with a checklist is received, access it via ``Message.media``:

.. code-block:: python

   @app.on_message(filters.checklist)
   async def on_checklist(client, message):
       checklist = message.checklist
       for task in checklist.tasks:
           status = "✅" if task.completed else "⬜"
           print(f"{status} {task.text}")
