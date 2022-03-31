#!/usr/bin/env python3
"""initialize"""
import numpy as np
def initialize(X, k):
 """ initializes cluster centroids for K-means"""
 if type(X) is not np.ndarray or X.ndim != 2:
      return None
 if type(k) is not int or k < 1:
      return None
d=X.shape[1]
min=np.amin(X,axis=0)
max=np.amax(X,axis=0)
centroides=np.random.uniform(low=min,high=max,size=(k,d))
return centroides
