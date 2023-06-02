import numpy as np
from scipy import linalg
import timeit

n = 1000

# 1로 채워진 사이즈 999짜리 밴드
band1 = np.ones((n-1), dtype=np.float64)
# 5로 채워진 사이즈 1000짜리 밴드
band2 = 5*np.ones((n,), dtype=np.float64)

b = np.ones((n,), dtype=np.float64)

# A full 행렬 생성
A_full = np.diag(band2) + np.diag(band1,k=1) + np.diag(band1,k=-1)

# solve 1000번 수행
start = timeit.default_timer()
for k in range(0,1000):
    x1 = linalg.solve(A_full,b)
end = timeit.default_timer()
computing_time = end - start
print("computing time for linalg.solve: ", computing_time)
print()

# lu_factor 이후 lu_solve 1000번 수행
start = timeit.default_timer()
lu, piv = linalg.lu_factor(A_full)
for k in range(0,1000):
    x2 = linalg.lu_solve( (lu,piv), b)
end = timeit.default_timer()
computing_time = end - start
print("computing time for linalg.lu_factor and lu_solve: ", computing_time)
print()

# x1 및 x2 타당성 검증
bp1 = A_full@x1
bp2 = A_full@x2
print(np.allclose(bp1, b))
print(np.allclose(bp2, b))
