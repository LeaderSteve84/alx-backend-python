#!/usr/bin/env python3
"""a module of a function that takes in an integer
max_delay and returns a asyncio.task.
"""


import asyncio
from random import uniform
from typing import Callable


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds
    (inclusive).
    Args:
        max_delay (int, optional): The max delay in seconds
        default value to 10
        return:
            float: The randomly generated delay.
    """

    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Callable:
    """
    Returns a asyncio.Task object.
    Args:
        max_delay (int): The maximum delay.

    Retun asyncio.create_task(wait_random(max_delay))
    """

    return asyncio.create_task(wait_random(max_delay))
