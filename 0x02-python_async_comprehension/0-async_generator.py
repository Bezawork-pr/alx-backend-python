#!/usr/bin/env python3
'''This files contains a async function
that loops 10 times and yields random number'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """Loops 10 times to yiels random float multiplied by 10"""
    for i in range(10):
        num = random.random() * 10
        yield num
        await asyncio.sleep(1)
