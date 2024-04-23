#!/usr/bin/env python3
"""a module of an asynchronous coroutine
that takes in an integer argument and
eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay=10):
    """Asynchronous coroutine.
    Args:
        max_delay (int): default value of 10
        return: float value
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
