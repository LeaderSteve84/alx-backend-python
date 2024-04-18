#!/usr/bin/env python3
"""modules that returns a tuple."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string k and the square
    of the int/float v as a float.
    """
    return (k, float(v ** 2))
