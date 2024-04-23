#!/usr/bin/env python3
"""a module of an asynchronous coroutine
that takes in an integer argument and
eventually returns it.
"""


import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[float] = 10) -> float:
    """Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds
    (inclusive).
    Args:
        max_delay (float, optional): The max delay in seconds
        default value to 10
        return:
            float: The randomly generated delay.
    """

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
