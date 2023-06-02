import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A1 = np.array([[1,-1],[-2,2],[2,-2]], dtype=np.float64)
A2 = np.array([[4,11,14],[8,7,-2]], dtype=np.float64)
A3 = np.random.rand(10,10)

# A1부터 A3까지 바꿔가며 이것저것 테스트 해보세요.
U, s, VT = linalg.svd(A1)
