#!/usr/bin/env python3
"""
Use mypy to validate the following piece
of code and apply any necessary changes"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
