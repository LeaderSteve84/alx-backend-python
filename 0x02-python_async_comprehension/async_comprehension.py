#!/usr/bin/env python3
"""Import async_generator from the previous
task and then write a coroutine called async
comprehension that takes no arguments.
"""


from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 random numbers using an async
    comprehension over async_generator, then returns the 10 random
    numbers.
    """
    return [i async for i in async_generator()]
