import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
# 1부터 10까지의 diagonal entry 1D array
band_diag = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.float64)
# 혹은 아래처럼 해도 됨
"""
band_diag = np.zeros((10,), dtype=np.float64)
for i in range(0,10):
    band_diag[i] = i+1
"""

# k=0 생략 가능
D = np.diag(band_diag, k=0)
P = np.random.rand(10,10) # 0~1
# 2배를 하면 0~2까지 random이고 그 이후에 모든 entry에 1을 빼주면 -1~1까지의 랜덤 행렬
P = 2*P -1
inv_P = linalg.inv(P)

# inv_P @ D @ P 로 하여도 고유치는 동일
A = P @ D @ inv_P

# eig 함수가 eigenvalue들을 순서대로 내주는줄 알았는데 아닙니다. 주의 해주세요.
eigvals = linalg.eig(A, right=False)
print(eigvals)

# 하지만 QR algorithm 자체는 norm이 큰 순서부터 나오는게 맞긴합니다.
Ak = A
for k in range(0,500):
    Q, R = linalg.qr(Ak)
    Ak = R @ Q
    print(k)
    prt(Ak, fmt="%0.10f")