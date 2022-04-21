#!/usr/bin/env python3
"""
This module contains the function poly_derivative(poly)
"""


def poly_derivative(poly):
    """This function calculates the derivative of a polynomial"""
    if type(poly) is not list or not len(poly):
        return None
    derivative = []
    for i, const in enumerate(poly):
        if i == 0 or i < len(poly) - 1:
            derivative.append(0)
        if i > 0 and const:
            derivative[i - 1] += i * const
    return derivative
