import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

b = np.ones( (3,), dtype=np.float64 )

A_sing = np.array( [ [1,3,4], [-4,2,-6], [-3,-2,-7] ], 
         dtype=np.float64)

A_gen = np.array( [ [0,1,2], [1,0,3], [4,-3,8] ], 
        dtype=np.float64)

A_sym = np.array( [ [1,2,1], [2,1,3], [1,3,1] ], 
        dtype=np.float64)

A_sym_c = np.array( [ [1,2-1j,1+2j], [2-1j,1,3], [1+2j,3,1] ], 
          dtype=np.complex128)

A_her = np.array( [ [1,2+1j,1-2j], [2-1j,1,3], [1+2j,3,1] ], 
        dtype=np.complex128)

A_pos = np.array( [ [2,-1,0], [-1,2,-1], [0,-1,2] ], 
        dtype=np.float64)

# 행렬을 바꿔가며 시도해보세요.
x = linalg.solve(A_pos,b, assume_a="gen")

# 해 출력
prt(x,fmt="%0.5e")
print()

# 나온 해를 통해 Ax를 해보고 b와 비교해보기
prt(A_pos@x-b,fmt="%0.5e")