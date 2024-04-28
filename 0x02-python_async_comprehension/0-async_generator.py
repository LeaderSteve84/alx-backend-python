#!/usr/bin/env python3
"""Module of corotine called async_generator
that takes no arguments.
"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that yields a random number between 0 and 10
    every second for 10 seconds.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
