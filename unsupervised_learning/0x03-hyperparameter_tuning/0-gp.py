#!/usr/bin/env python3

import numpy as np


class GaussianProcess:
    """initialize GaussianProcess"""
    def __init__(self, X, Y, l=1, sigma_f=1):
        """ constructor of the class"""
        self.X = X
        self.Y = Y
        self.l = l
        self.sigma_f = sigma_f
        self.K = self.kernel(X, X)

    def kernel(self, X1, X2):
        """calculates vthe kernel function"""
        s = (self.sigma_f ** 2)
        K = s * np.exp(np.square(X1 - X2.T) / -(2 * (self.l ** 2)))
        return K
