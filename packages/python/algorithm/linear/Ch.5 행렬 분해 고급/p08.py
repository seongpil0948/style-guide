import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import matmul_banded

lbw = 2
ubw = 1

A_band = np.array([[0,2,2,2,1],[1,1,1,1,1],[1,1,1,1,0],[2,2,2,0,0]]
        ,dtype=np.float64)
dummy_array = np.zeros( (lbw, A_band.shape[1]), dtype=np.float64 )
A_band_LU = np.vstack((dummy_array,A_band))

b = np.ones((5,),dtype=np.float64)

gbtrf = linalg.get_lapack_funcs("gbtrf",dtype=np.float64)
gbtrs = linalg.get_lapack_funcs("gbtrs",dtype=np.float64)

LU_band, piv, info = gbtrf(A_band_LU, lbw, ubw)
print("gbtrf info:", info)

x, info = gbtrs(LU_band, lbw, ubw, b, piv)
print("gbtrs info:", info)

bp = matmul_banded((lbw,ubw), A_band, x)

print(np.allclose(bp,b))
