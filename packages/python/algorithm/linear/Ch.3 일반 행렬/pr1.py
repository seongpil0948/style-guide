import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

# Hilbert 행렬 생성
A = linalg.hilbert(10)

b = np.ones((10,),dtype=np.float64)

# Hilbert 행렬 구경
prt(A, fmt="%0.5f")

# direct inversion
inv_A = linalg.inv(A)

x1 = inv_A @ b

x2 = linalg.solve(A,b)

# direct inversion 해의 정확도 구경
prt(A@x1-b, fmt="%0.15e")
print()

# solve 기능 (LUx=b를 푸는)의 해의 정확도 구경
prt(A@x2-b, fmt="%0.15e")
print()

# zero vector
zr = np.zeros((10,),dtype=np.float64)

# x1 비교
print(np.allclose(A@x1-b,zr))

# x2 비교
print(np.allclose(A@x2-b,zr))

# 힐버트 행렬 사이즈를 늘리면 solve로도 부정확하게 풀린다는걸 알 수 있음. 궁금하면 테스트 해보기!
