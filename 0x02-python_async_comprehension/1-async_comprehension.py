#!/usr/bin/env python3
'''This file imports async_generator from the previous task
then write a coroutine called async_comprehension that takes no arguments'''
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    '''Return yields from async_generator'''
    result = []
    async for i in async_generator():
        result.append(i)
    return result
