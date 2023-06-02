import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[2,4,-1,5,-2],[-4,-5,3,-8,1],[2,-5,-4,1,8],[-6,0,7,-3,1]],
    dtype=np.float64)

P, L, U = linalg.lu(A)

prt(L,fmt="%0.1f")
print()
prt(U,fmt="%0.1f")
print()
prt(P,fmt="%0.1f")
print()
prt(P@L@U,fmt="%0.1f")
