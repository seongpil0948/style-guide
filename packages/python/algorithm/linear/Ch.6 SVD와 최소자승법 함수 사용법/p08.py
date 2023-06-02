import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[1,-1],[-2,2],[2,-2]],dtype=np.float64)

U, s, VT = linalg.svd(A)
r = s.shape[0] - sum(np.allclose(lx,0) for lx in s)

Vr = VT[ :r, :].T
Ur = U[ :, :r ]
D = np.diag(s[:r])

pinv_A = linalg.pinv(A)
prt(pinv_A,fmt="%0.5e")
print()

# pseudoinverse 직접 구하기
rpinv_A = Vr@linalg.inv(D)@Ur.T
print()
prt(rpinv_A,fmt="%0.5e")
