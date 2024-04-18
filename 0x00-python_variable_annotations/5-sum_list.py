#!/usr/bin/env python3
"""module of type-annotated function that
returns the sum of floats arguments as
a float
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats and return the result."""
    return sum(input_list)
