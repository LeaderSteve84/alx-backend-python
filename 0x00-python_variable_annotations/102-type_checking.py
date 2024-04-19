#!/usr/bin/env python3
""""""


from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array: Tuple[Any, ...] = (12, 72, 91)

zoom_2x: Tuple[Any, ...] = zoom_array(array)

zoom_3x: Tuple[Any, ...] = zoom_array(array, 3)
