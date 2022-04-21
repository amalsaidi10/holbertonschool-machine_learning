#!/usr/bin/env python3
"""
This module contains the function summation_i_squared(n)
"""


def summation_i_squared(n):
    """This function calculates the sum of i^2 from i=1 to n"""
    if type(n) is not int or n < 1:
        return None
    return int(n*(n+1)*(2*n+1)/6)
