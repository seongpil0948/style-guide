import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array( [[1,3,3],[-3,-5,-3],[3,3,1]], dtype=np.float64 )

eigvals = linalg.eig(A, right=False)
prt(eigvals)

Ak = A
for k in range(0,50):
    Q, R = linalg.qr(Ak)
    Ak = R @ Q
    print(k)
    prt(Ak, fmt="%0.10f")
    # 변화가 적음을 판단하여 for 문을 break하게 짜는게 더 현명하지만 본 수업에서는 그냥 관측만 해봄.