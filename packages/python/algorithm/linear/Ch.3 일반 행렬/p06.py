import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array( [ [1,2,1], [2,1,3], [1,3,1] ],
    dtype=np.float64 )

inv_A = linalg.inv(A)

prt(inv_A, fmt="%0.2f")
print()

# inverse가 맞는지 확인해봅시다.
prt(inv_A @ A, fmt="%0.1f")
print()
prt(A @ inv_A, fmt="%0.1f")