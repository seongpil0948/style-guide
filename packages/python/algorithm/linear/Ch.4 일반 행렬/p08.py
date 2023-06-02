import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
import timeit
from custom_linalg import eigh

A = np.array([[6,3,1,5],[3,0,5,1],[1,5,6,2],[5,1,2,2]],
    dtype=np.float64)

# timeit을 사용하여 시작 시간과 끝 시간을 기록하여 계산 시간을 구할 수 있음.
start = timeit.default_timer()
eigvals, eigvecs = linalg.eigh(A)
# 아래는 우리가 배운 고유치 계산 이론을 사용하도록 하는 함수, 작은 행렬의 경우는 불필요한 부분이 생략되어 오히려 속도는 빠를 수 있음.
#eigvals, eigvecs = eigh(A)
end = timeit.default_timer()
computing_time = end-start
print("computing time:", computing_time)
print()

prt(eigvals, fmt="%0.5e")
print()
prt(eigvecs, fmt="%0.5e")
print()

comp1 = A@eigvecs
comp2 = eigvecs*eigvals

print(np.allclose(comp1,comp2))