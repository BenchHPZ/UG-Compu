from helper import *

import sys
import scipy

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from scipy.linalg import solve_triangular 

NOTEBOOK = True

def metodo_newton_horner(n, a, x0, N, t=None, dtype=np.float64):
    if t == None:
        t = np.finfo(dtype).eps
        
    c = np.array(a, dtype=dtype, copy=True)
    r = np.array(a, dtype=dtype, copy=True)
    
    for m in range(n):
        x = x0
        res = False
        for k in range(N):
            px, b = metodo_horner(n-m-1, c, x, dtype=dtype)
            if abs(px) < t:
                r[m-1] = x
                c = np.copy(b)
                res = True
                break
            else:
                dpx, b = metodo_horner(n-m, b, x)
                x = x - px/dpx
        
        if res == False:
            m = m-1
            break
            
    return r, m



