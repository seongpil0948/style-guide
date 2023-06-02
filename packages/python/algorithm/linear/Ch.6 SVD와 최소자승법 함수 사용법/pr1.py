import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.random.rand(20,10)

b = np.random.rand(20)

U, s, VT = linalg.svd(A)

r = s.shape[0] - sum(np.allclose(lx,0) for lx in s)
print(r)

ColA = linalg.orth(A)
NullA = linalg.null_space(A)

# rank를 구한뒤 (r) 직접 column space 확인
prt(U[:,:r])
print()
# 기본 기능
prt(ColA)
print()

# null space, 현재는 row가 두배나 많아서 null space가 없을 확률이 높음
# row를 5개로 줄이는 식으로 테스트 해보면 좋을 듯 합니다. 이것 저것 바꿔보세요.
prt(VT[r:,:].T)
print()
# 기본 기능
prt(NullA)

x_hat, res, rank, s = linalg.lstsq( A, b )

prt(A@x_hat)
print()
prt(b)
print()

# residual
print(res)