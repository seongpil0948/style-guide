import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A1 = np.array([[9,1,1],[1,0,-1],[1,-1,4]],dtype=np.float64)

A2 = np.array([[9,1+1j,1],[1+1j,0,-1-2j],[1,-1-2j,4]],dtype=np.complex128)

# A1 부터 테스트
L, D, perm = linalg.ldl( A1, lower=True, hermitian=False )

PAP = A1[perm,:][:,perm]
# P를 아래처럼 정의하고 사용 가능
#P = np.identity(3)[perm,:]

PL = L[perm,:]
right = PL@D@PL.T

# L이 아닌 PL이 lower triangular matrix
prt(PL, fmt="%0.2e")
print()
print( np.allclose(PAP,right) )
print()

# A2
L, D, perm = linalg.ldl( A2, lower=True, hermitian=False )

PAP = A2[perm,:][:,perm]

PL = L[perm,:]
right = PL@D@PL.T

prt(PL, fmt="%0.2e")
print()
print( np.allclose(PAP,right) )
