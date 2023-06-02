import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.tri(4,3,k=0,dtype=np.float64)

Q, R = linalg.qr(A, mode="economic")

prt(Q, fmt="%0.6f")
print()
prt(R, fmt="%0.6f")
print()
prt(Q@R, fmt="%0.17f")
print(np.allclose(A,Q@R))
