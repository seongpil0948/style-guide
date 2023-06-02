import numpy as np
from print_lecture import print_custom as prt

# k=0 생략 가능
A1 = np.eye(3, 4, k=0, dtype=np.float64)

A2 = np.eye(4, 3, k=1, dtype=np.float64)

# A2와 동일
A3 = np.identity(3, dtype=np.float64)
#A3의 동일 표현
#A3 = np.eye(3, dtype=np.float64)
#A3 = np.eye(3, 3, dtype=np.float64)

prt(A1, fmt="%0.1f")
print()
prt(A2, fmt="%0.1f")
print()
prt(A3, fmt="%0.1f")
