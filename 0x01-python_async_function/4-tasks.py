#!/usr/bin/env python3
"""that takes the code from wait_n
and alter it into a new function.
"""


import asyncio
from random import uniform
from typing import List
from asyncio import as_completed, Task


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


def task_wait_random(max_delay: int = 10) -> Task:
    """
    Returns a asyncio.Task object.
    Args:
        max_delay (int): The maximum delay.

    Retun asyncio.create_task(wait_random(max_delay))
    """

    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay.

    Return:
        List[float]: The list of all the delays in ascending order.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
