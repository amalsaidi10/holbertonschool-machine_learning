#!/usr/bin/env python3
import numpy as np
kmeans = __import__('1-kmeans').kmeans
def initialize(X, k):
    """initializes variables for a Gaussian Mixture Model"""
    if type(X) is not np.ndarray or X.ndim != 2:
        return None, None, None
    if type(k) is not int or k < 1:
        return None, None, None

    _,  d = X.shape
    pi = np.full(k, 1/k) # a new array of shape k filled with 1/k
    m, _ = kmeans(X, k)
      
    S = np.tile(np.eye(d), (k, 1, 1))
    return pi, m, S
