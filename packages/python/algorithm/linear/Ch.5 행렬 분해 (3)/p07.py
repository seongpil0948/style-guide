import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.random.rand(10,10)

H, U = linalg.hessenberg( A, calc_q = True )

prt(A,fmt="%0.5f")
print()
prt(H,fmt="%0.5f")
print()
prt(U,fmt="%0.5f")

print(np.allclose(A, U@H@U.T))

# orthonormal (unitary) 한지 확인해보기, U* U = zero matrix 여야함
np.allclose( U.T @ U , np.zeros((10,10)) )
