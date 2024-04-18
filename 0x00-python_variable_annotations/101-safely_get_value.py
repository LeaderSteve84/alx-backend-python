#!/usr/bin/env python3
"""module that add type annotation to the given function"""


from typing import Mapping, Any, Union, TypeVar


# Define a TypeVar for the return type
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Get a value from a dictionary safely with a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
