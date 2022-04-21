#!/usr/bin/env python3
"""
integral
"""


def poly_integral(poly, C=0):
  """
   calculates the integral of a polynomial
  """
  if type(poly) is not list or not len(poly)or type(C) is not int:
        return None
  integral = [C]
  if poly == [0]:
    return integral
  for i, val in enumerate(poly):
      result = val / (i + 1)
      if int(result) == result :
          result=int(result)
     else:
          result
    integral.append(result)
  return integral
