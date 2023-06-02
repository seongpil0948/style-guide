import numpy as np
from scipy import linalg
import timeit

# 작은 값에서 큰 값으로 변화 시켜보면서 테스트해보면 재밌습니다.
n = 10000

# 사이즈 9999 모두 1
band_off1 = np.ones((n-1,), dtype=np.complex128)

# 사이즈 9998 모두 i
band_off2 = 1j*np.ones((n-2,), dtype=np.complex128)

# 사이즈 10000 모두 5
band_diag = 5*np.ones((n,), dtype=np.complex128)

# full matrix
A_full = np.diag(band_diag) + np.diag(band_off1, k=1) + np.diag(band_off2, k=2) + np.diag(band_off1, k=-1) - np.diag(band_off2, k=-2)

# upper band matrix for cholesky_banded
zr = np.zeros((1,), dtype=np.complex128)
row1 = np.hstack((zr,zr,band_off2))
row2 = np.hstack((zr,band_off1))
# row 3는 생략 band_diag와 동일
A_band_h = np.vstack( (row1,row2,band_diag) )

b = np.ones((n,), dtype=np.complex128)

# lu_factor
start = timeit.default_timer()
lu, piv = linalg.lu_factor(A_full)
end = timeit.default_timer()
print("computing time for lu_factor: ", end - start)

# lu_solve
start = timeit.default_timer()
x1 = linalg.lu_solve((lu,piv),b)
end = timeit.default_timer()
print("computing time for lu_solve: ", end - start)
print()

# cholesky
start = timeit.default_timer()
R = linalg.cholesky(A_full, lower=False)
end = timeit.default_timer()
print("computing time for cholesky: ", end - start)

# cho_solve
start = timeit.default_timer()
x2 = linalg.cho_solve((R,False),b)
end = timeit.default_timer()
print("computing time for cho_solve: ", end - start)
print()

# cholesky_banded
start = timeit.default_timer()
R_band = linalg.cholesky_banded(A_band_h, lower=False)
end = timeit.default_timer()
print("computing time for cholesky: ", end - start)

# cho_solve_banded
start = timeit.default_timer()
x3 = linalg.cho_solve_banded((R_band,False),b)
end = timeit.default_timer()
print("computing time for cho_solve_banded: ", end - start)
print()

# x1, x2, x3 다 수치적으로 비슷한지 간단히 확인
print(np.allclose(x1,x2))
print(np.allclose(x2,x3))
