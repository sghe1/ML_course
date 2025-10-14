# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    N,_ = tx.shape
    A = tx.T @ tx
    b = tx.T @ y 
    w = np.linalg.solve(A,b)
    error = 1/(N) * np.linalg.norm(y - tx.dot(w)) ** 2
    error = float(error)
    return w, error
