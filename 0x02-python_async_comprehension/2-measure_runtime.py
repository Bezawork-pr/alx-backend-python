#!/usr/bin/env python3
'''This file contains a function that
imports async_comprehension from the previous file
and write a measure_runtime'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Calculate time taken'''
    start_time = time.monotonic()
    my_list = [async_comprehension() for i in range(4)]
    await asyncio.gather(*my_list)
    end_time = time.monotonic()
    return end_time - start_time
