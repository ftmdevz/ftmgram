import asyncio
from typing import List
import ftmgram


class MultiClient:
    """Orchestrator for managing and running multiple FTMGram clients concurrently.

    Example:
        .. code-block:: python

            from ftmgram import Client
            from ftmgram.helpers import MultiClient

            bot1 = Client("bot_1", bot_token="TOKEN_1")
            bot2 = Client("bot_2", bot_token="TOKEN_2")
            user = Client("my_account")

            multi = MultiClient([bot1, bot2, user])
            multi.run()
    """

    def __init__(self, clients: List["ftmgram.Client"]):
        self.clients = clients

    async def start(self):
        """Start all registered clients concurrently."""
        tasks = [client.start() for client in self.clients]
        await asyncio.gather(*tasks)

    async def stop(self):
        """Stop all registered clients gracefully."""
        tasks = [client.stop() for client in self.clients if client.is_connected]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def idle(self):
        """Keep the event loop running until SIGINT or SIGTERM is received."""
        await ftmgram.idle()

    def run(self):
        """Start all clients and block until stopped."""
        loop = asyncio.get_event_loop()

        async def _main():
            await self.start()
            await self.idle()
            await self.stop()

        try:
            loop.run_until_complete(_main())
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            loop.run_until_complete(self.stop())
