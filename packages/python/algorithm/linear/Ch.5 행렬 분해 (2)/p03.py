import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A1 = np.array( [[1,-2j],[2j,5]], dtype=np.complex128)
b1 = np.ones((2,), dtype = np.float64)

A2 = np.array( [[1,-1,0],[-1,2,-1],[0,-1,3]], dtype=np.float64 )
b2 = np.ones((3,), dtype = np.float64)

# A1 테스트
R1 = linalg.cholesky(A1, lower=False)
# Cholesky decomposition 잘됐는지 한번 확인
prt(R1.T @ R1, fmt="%0.0f")
print()
x1 = linalg.cho_solve( (R1, False), b1 )
# 해 제대로 나왔는지 확인
print(np.allclose(A1@x1, b1))
print()

# A2 테스트
R2 = linalg.cholesky(A2, lower=False)
# Cholesky decomposition 잘됐는지 한번 확인
prt(R2.T.conjugate() @ R2, fmt="%0.0f")
print()
x2 = linalg.cho_solve( (R2, False), b2 )
# 해 제대로 나왔는지 확인
print(np.allclose(A2@x2, b2))
