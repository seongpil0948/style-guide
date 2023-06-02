import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[1,3,4],[-4,2,-6],[-3,-2,-7]])
b = np.array([1,1,1])

x_hat, res, rank, s = linalg.lstsq( A, b )

prt(x_hat)
print()
prt(A@x_hat)
print()
print(res)