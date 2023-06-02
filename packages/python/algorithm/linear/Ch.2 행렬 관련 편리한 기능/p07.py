import numpy as np
from print_lecture import print_custom as prt

A1 = np.zeros( (2,3), dtype=np.float64)

A2 = np.ones( (2,2), dtype=np.float64 )

A3 = np.full( (3,3), 1+1j, dtype=np.complex128)


prt(A1, fmt="%0.1f")
print()
prt(A2, fmt="%0.1f")
print()
prt(A3, fmt="%0.1f")
