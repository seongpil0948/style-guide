import numpy as np
from scipy import linalg
from custom_sp import matmul_toeplitz
import timeit

c = np.array( [1,3,6,10], dtype=np.float64 )
r = np.array( [1,-1,-2,-3], dtype=np.float64)

b = np.ones((4,), dtype=np.float64)

x = linalg.solve_toeplitz( (c,r), b )

bp = matmul_toeplitz( (c,r), x )

print( np.allclose(bp,b) )

recon_t = linalg.toeplitz(c,r)
print(recon_t)