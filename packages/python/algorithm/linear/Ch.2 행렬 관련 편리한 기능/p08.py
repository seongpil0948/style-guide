import numpy as np
from print_lecture import print_custom as prt

# type 옵션 없음, 기본값 np.float64, 0~1사이
A = np.random.rand(3,5)

prt(A, fmt="%0.4f")
