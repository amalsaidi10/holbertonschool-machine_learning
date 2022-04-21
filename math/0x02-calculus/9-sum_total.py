#!/usr/bin/env python3
"""recursive method"""


def summation_i_squared(n):
    if n < 1:
        return None
    if n == 1:
        return 1
    return n ** 2 + summation_i_squared(n - 1)
  
