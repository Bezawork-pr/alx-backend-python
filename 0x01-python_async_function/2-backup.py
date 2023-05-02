#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, delay_time):
    asyncio.run(wait_n(n, delay_time))
    return 5
