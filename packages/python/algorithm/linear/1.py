import numpy as np

A = np.array( [ [1,2,4,1], [2,1,3,1], [5,2,1,4] ], dtype=np.float64 )

print(A)
print(A.shape)

# 오류 발생
#A[0,2] = 1+2j
#A[2,1] = 1+2j

# 0으로 바꿔보기
A[0,2] = 0
A[2,1] = 0

print(A)