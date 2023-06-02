import numpy as np
from print_lecture import print_custom as prt

# random real 행렬
A = np.random.rand(3,3)

# 명시적 타입 변환
A = A.astype(dtype=np.complex128)

# 1i를 scalar 곱을 해줘서 엔트리 모두 허수로 만들기
A = 1j*A

# 허수부분만 0i~1i인걸 알 수 있음
prt(A, fmt="%0.4f")
