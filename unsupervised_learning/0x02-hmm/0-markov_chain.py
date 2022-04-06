#!/usr/bin/env python3
import numpy as np

def markov_chain(P, s, t=1):
  """
    new_state
  """
  n= P.shape[0]
  d= P.shape[1]
  if type(P) is not np.ndarray or P.ndim!=2 or n!= d :
    return None
  if not np.allclose(np.sum(P, axis=1), 1) :
        return None
  if type(s) is not np.ndarray or s.shape[0]!= 1 or s.shape[1]!= P.shape[0] :
    return None
  if t < 1 or type(t) is not int :
    return None
  product=np.linalg.matrix_power(P , t)
  return np.matmul(s , product)

