import numpy as np
from scipy import linalg
from custom_band import matmul_banded_h

A_band_h = np.array( [[0,0,1j,2,3j],[0,-1,-2,3,4],[9,8,7,6,9]],
         dtype=np.complex128 )
b = np.ones((5,),dtype=np.float64)

R_band_h = linalg.cholesky_banded( A_band_h, lower=False )

x = linalg.cho_solve_banded( (R_band_h, False), b )

bp = matmul_banded_h(2, A_band_h, x)
print(np.allclose(bp,b))

# 아래는 R을 재구축해서 기존 cho_solve 사용해서 문제 풀어보기
Rr1 = R_band_h[0,2:]
Rr2 = R_band_h[1,1:]
Rr3 = R_band_h[2,:]

R_full = np.diag(Rr3) + np.diag(Rr2,k=1) + np.diag(Rr1,k=2)
x1 = linalg.cho_solve( (R_full, False), b )
# A = R* R 그러므로 , bp = Ax = R* R x
bp = R_full.T.conjugate()@R_full@x1
print(np.allclose(bp,b))
