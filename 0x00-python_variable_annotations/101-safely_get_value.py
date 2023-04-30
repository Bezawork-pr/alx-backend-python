#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function"""
from typing import TypeVar, Mapping, Any, Union, Optional
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[Union[T, None]]
                     = None) -> Union[Any, T]:
    """Returns Key"""
    if key in dct:
        return dct[key]
    else:
        return default
