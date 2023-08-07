#!/usr/bin/env python3

""" Measure the runtime. """

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    total_time = await wait_n(n, max_delay)
    end_time = time.time()

    elapsed_time = end_time - start_time

    avg_time = elapsed_time / n
    return avg_time
