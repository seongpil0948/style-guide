import numpy as np
from scipy import linalg
from custom_band import read_banded_h, matmul_banded_eig, matmul_banded_h
import timeit

n = 1000

diagonals = 3*np.ones((n,))
off_diagonals = np.ones((n-1,))

A_full = np.diag(diagonals) + np.diag(off_diagonals,k=1) + np.diag(off_diagonals,k=-1)

zr = np.zeros((1,))
band_row0 = np.hstack( (zr,off_diagonals) )

# 반쪽 upper 밴드 행렬
A_band = np.vstack( (band_row0,diagonals) )

# eigh 계산 속도 측정
start = timeit.default_timer()
eigvals_full, eigvecs_full = linalg.eigh(A_full)
end = timeit.default_timer()
print("computing time, full matrix: ",end-start)
print()

# eigh 제대로 나왔나 확인
comp1 = A_full @ eigvecs_full
comp2 = eigvecs_full * eigvals_full
print(np.allclose(comp1,comp2))
print()

# 밴드 행렬의 경우 계산 속도 측정
start = timeit.default_timer()
eigvals_band, eigvecs_band = linalg.eig_banded(A_band, lower=False)
end = timeit.default_timer()
print("computing time, band matrix: ",end-start)
print()

# 커스텀 함수의 느림을 확인 ㅠㅠ
start = timeit.default_timer()
comp1 = matmul_banded_eig(1,A_band,eigvecs_band,lower=False)
end = timeit.default_timer()
print("computing time, matmul: ",end-start)
print()
comp2 = eigvecs_band * eigvals_band
# 제대로 나왔는지 확인
print(np.allclose(comp1,comp2))
