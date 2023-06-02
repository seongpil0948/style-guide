import numpy as np
from print_lecture import print_custom as prt


A1 = np.tri(4, 3, k=-1, dtype=np.float64)

# k=0 생략 가능
A2 = np.eye(4, 4, k=0, dtype=np.float64)

prt(A1, fmt="%0.1f")
print()
prt(A2, fmt="%0.1f")
