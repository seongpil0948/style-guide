import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[1,0,0,0],[1,4,0,0],[5,0,1,0],[8,1,-2,2]],
    dtype=np.float64)

b = np.array([1,2,3,4],dtype=np.float64)

x = linalg.solve_triangular(A,b,lower=True)

prt(x,fmt="%0.5e")
print()
prt(A@x-b, fmt="%0.5e")