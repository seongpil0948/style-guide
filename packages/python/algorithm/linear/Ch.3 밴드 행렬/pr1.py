import numpy as np
from scipy import linalg
from custom_band import matmul_banded_h
# 미리 정의
n = 1000

# 1로 채워진 사이즈 999짜리 밴드
band1 = np.ones((n-1), dtype=np.float64)

# 2로 채워진 사이즈 1000짜리 밴드
band2 = 2*np.ones((n,), dtype=np.float64)

b = np.ones((n,), dtype=np.float64)

# A full 행렬 생성
A_full = np.diag(band2) + np.diag(band1,k=1) + np.diag(band1,k=-1)

# 사이즈 1짜리 zero vector
zr = np.zeros((1,), dtype=np.float64)

# A의 upper band 형태를 만들기 위한 작업
row1 = np.hstack( (zr,band1) ) # 0,1,1,1,......,1
# row2는 band2와 동일하니깐 생략

# upper band 형태
A_band_h = np.vstack( (row1,band2) )

# full matrix로 해를 구하기, 옵션은 일단 생략하였으나, positive definite 성질 사용 가능 (assume_a="pos")
x1 = linalg.solve(A_full,b)

x2 = linalg.solveh_banded(A_band_h,b)

# x1 및 x2 타당성 검증
bp1 = A_full@x1
bp2 = matmul_banded_h(1,A_band_h,x2,lower=False)
print(np.allclose(bp1, b))
print(np.allclose(bp2, b))