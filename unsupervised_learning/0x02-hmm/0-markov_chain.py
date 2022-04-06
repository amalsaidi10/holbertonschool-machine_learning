#!/usr/bin/env python3
import numpy as np

def markov_chain(P, s, t=1):
  """
     P is a square 2D numpy.ndarray of shape (n, n) representing the transition matrix
     P[i, j] is the probability of transitioning from state i to state j
     n is the number of states in the markov chain
     s is a numpy.ndarray of shape (1, n) representing the probability of starting in each state
     t is the number of iterations that the markov chain has been through
    Returns: a numpy.ndarray of shape (1, n)
    representing the probability of being in a specific state after t iterations, or None on failure
 """
  n= P.shape[0]
  d=P.shape[1]
  if type(P) is not np.ndarray or P.ndim!=2 or n!= d :
    return None
  if not np.allclose(np.sum(P, axis=1), 1):
        return None
  if type(s) is not np.ndarray or s.shape[0]!=1 or s.shape[1]!=P.shape[0]:
    return None
  if t <1 or type(t)  is not int :
    return None
  product=np.linalg.matrix_power(P,t)
  
  return np.matmul(s,product)
