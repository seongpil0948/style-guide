import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

b = np.ones( (3,), dtype=np.float64 )

A = np.array( [ [2,-1,0], [-1,2,-1], [0,-1,2] ], 
        dtype=np.float64)

x = linalg.solve(A,b,assume_a="pos")

prt(x,fmt="%0.5e")
print()
prt(A@x-b,fmt="%0.5e")

zr = np.zeros((3,),dtype=np.float64)

# 0벡터와 비교, 이 경우엔 기본값을 생각해보면 Ax-b의 각각 entry의 절대값이 1e-8 보다 작으면 true 반환
bool_close = np.allclose( A@x-b, zr )
print(bool_close)

# 혹은 Ax와 b를 비교해도 됨
bool_close = np.allclose( A@x, b )
print(bool_close)