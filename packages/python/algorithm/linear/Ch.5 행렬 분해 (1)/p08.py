import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[7,5,6,6],[1,2,2,8],[5,4,4,8],[9,5,8,7]],
    dtype=np.float64)

b = np.ones((4,),dtype=np.float64)

lu, piv = linalg.lu_factor(A)
x = linalg.lu_solve( (lu,piv), b )

prt(x,fmt="%0.4e")
print()
print(np.allclose(A@x, b))
