import numpy as np
from scipy import linalg
from custom_sp import matmul_circulant

c = np.array( [2,-1,0,1,0,0,1], dtype=np.float64 )

b = np.ones((7,), dtype=np.float64)

x = linalg.solve_circulant( c, b )

bp = matmul_circulant(c,x)

print(np.allclose(bp,b))

recon_c = linalg.circulant(c)

print(recon_c)