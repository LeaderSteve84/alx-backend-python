#!/usr/bin/env python3
"""Module that async routine that returns
a float.
"""


import asyncio
import time
from typing import List
from random import uniform
from asyncio import as_completed


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


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawns wait_random n times
        with the specified max_delay.

    Return:
        List[float]: The list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return total_time / n.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay.

    Returns:
        float: The average time of execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
