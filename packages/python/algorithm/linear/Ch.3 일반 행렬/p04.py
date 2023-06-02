import numpy as np
from scipy import linalg

A1 = np.array( [ [1,5,0], [2,4,-1], [0,-2,0]],
     dtype=np.float64 )

A2 = np.array( [ [1,-4,2], [-2,8,-9], [-1,7,0]],
     dtype=np.float64 )

det1 = linalg.det(A1)
det2 = linalg.det(A2)

print(det1)
print(det2)