#!/usr/bin/env python3
"""modules that returns a function
that multiples a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiples a float by the specified multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
