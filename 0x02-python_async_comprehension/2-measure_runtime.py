#!/usr/bin/env python3
"""Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async
comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""


import asyncio
import time
from typing import List

# Import the async_comprehension function from the previous task
from async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension four times in
    parallel and measures the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
