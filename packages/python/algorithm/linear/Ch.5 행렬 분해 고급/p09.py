import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import matmul_banded
import timeit
lbw = 1
ubw = 1
n = 5000

band_1 = np.ones( (n-1,), dtype=np.float64 )
band_d = 5*np.ones( (n,), dtype=np.float64 )

zr = np.zeros((1,),dtype=np.float64)
up = np.hstack( (zr,band_1) )
down = np.hstack( (band_1,zr) )

A_band = np.vstack( (up,band_d,down) )
dummy_array = np.zeros( (lbw, A_band.shape[1]), dtype=np.float64 )
A_band_LU = np.vstack((dummy_array,A_band))

b = np.ones((n,),dtype=np.float64)

gbtrf = linalg.get_lapack_funcs("gbtrf",dtype=np.float64)
gbtrs = linalg.get_lapack_funcs("gbtrs",dtype=np.float64)

start = timeit.default_timer()
LU_band, piv, info = gbtrf(A_band_LU, lbw, ubw)
end = timeit.default_timer()
print("LU band decomp:", end-start)

start = timeit.default_timer()
x, info = gbtrs(LU_band, lbw, ubw, b, piv)
end = timeit.default_timer()
print("LU band solve:", end-start)


A_full = np.diag(band_d) + np.diag(band_1,k=1) + np.diag(band_1,k=-1)

start = timeit.default_timer()
lu, piv = linalg.lu_factor( A_full )
end = timeit.default_timer()
print("LU full decomp:", end-start)

start = timeit.default_timer()
x_full = linalg.lu_solve( (lu,piv), b )
end = timeit.default_timer()
print("LU full solve:", end-start)

print(np.allclose(x,x_full))