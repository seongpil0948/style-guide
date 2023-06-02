import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[1,-1],[-2,2],[2,-2]],dtype=np.float64)

ColA = linalg.orth(A)
NullA = linalg.null_space(A)

prt(ColA, fmt="%0.5f")
print(ColA.shape)
print()
prt(NullA, fmt="%0.5f")
print(NullA.shape)