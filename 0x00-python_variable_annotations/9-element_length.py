#!/usr/bin/env python3
"""module that returns the values with
the appropriate types.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuples where each tuple
    contains a sequence from lst and its length.
    """
    return [(i, len(i)) for i in lst]
