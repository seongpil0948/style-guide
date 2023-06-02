import numpy as np
from scipy import linalg
import timeit

n = 1000

# 사이즈 999 모두 1
band_off1 = np.ones((n-1,), dtype=np.float64)

# 사이즈 998 모두 1
band_off2 = np.ones((n-2,), dtype=np.float64)

# 사이즈 1000 모두 2
band_diag = 2*np.ones((n,), dtype=np.float64)

# full matrix
A_full = np.diag(band_diag) + np.diag(band_off1, k=1) + np.diag(band_off2, k=2) + np.diag(band_off1, k=-1) + np.diag(band_off2, k=-2)

# linalg.eig
start = timeit.default_timer()
eigvals1, eigvecs1 = linalg.eig(A_full)
end = timeit.default_timer()
computing_time = end - start
print("computing time for eig: ", computing_time)
print()

# linalg.eigh
start = timeit.default_timer()
eigvals2, eigvecs2 = linalg.eigh(A_full)
end = timeit.default_timer()
computing_time = end - start
print("computing time for eigh: ", computing_time)
print()

# 타당성 검증
print(np.allclose(A_full@eigvecs1, eigvecs1*eigvals1))
print(np.allclose(A_full@eigvecs2, eigvecs2*eigvals2))