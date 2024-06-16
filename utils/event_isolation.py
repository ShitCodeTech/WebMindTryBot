from aiogram.fsm.middleware import BaseEventIsolation
import asyncio
from contextlib import asynccontextmanager

class CustomEventIsolation(BaseEventIsolation):
    def __init__(self):
        self._locks = {}

    @asynccontextmanager
    async def lock(self, key: str):
        if key not in self._locks:
            self._locks[key] = asyncio.Lock()
        async with self._locks[key]:
            yield

    async def close(self):
        self._locks.clear()
