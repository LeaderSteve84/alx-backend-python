#!/usr/bin/env python3
"""modules that ..."""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the sequence lst,
       or None if lst is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
