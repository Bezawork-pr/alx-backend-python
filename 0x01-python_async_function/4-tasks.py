#!/usr/bin/env python3
"""Modify 3-tas function"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait till complete a created task"""
    my_list = []
    new_list = []
    for i in range(n):
        tasks = task_wait_random(max_delay)
        my_list.append(tasks)
    new_list = [await task for task in asyncio.as_completed(my_list)]
    return new_list
