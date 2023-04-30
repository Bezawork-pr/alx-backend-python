#!/usr/bin/env python3
"""This file contains variables type annotation"""
from typing import List, Any


def sum_mixed_list(mxd_lst: List[Any]) -> float:
    """Sums a list of mixed numbers"""
    return sum(mxd_lst)
