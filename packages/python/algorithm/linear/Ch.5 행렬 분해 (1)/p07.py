import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_decomp import perm_from_piv

A = np.array([[7,5,6,6],[1,2,2,8],[5,4,4,8],[9,5,8,7]],
    dtype=np.float64)

lu, piv = linalg.lu_factor( A )

prt(lu, fmt="%0.3f")
print()
L = np.tril(lu,k=-1) + np.identity(4)
prt(L,fmt="%0.3f")

U = np.triu(lu)
print()
prt(L@U,fmt="%0.3f")

perm = perm_from_piv(piv)
P = np.identity(4)[perm,:]
print()

prt(P@L@U,fmt="%0.3f")