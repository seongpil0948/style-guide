import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import read_banded, matmul_banded

b = np.ones((5,),dtype=np.float64)

band_a1 = read_banded("p06_inp1.txt",(2,1),
         dtype=np.float64, delimiter=" ")

band_a2 = read_banded("p06_inp2.txt",(1,1),
         dtype=np.float64, delimiter=" ")

x1 = linalg.solve_banded( (2,1), band_a1, b )
x2 = linalg.solve_banded( (1,1), band_a2, b )

prt(x1,fmt="%0.4e")
bp1 = matmul_banded( (2,1), band_a1, x1 )
print(np.allclose(bp1, b))

prt(x2,fmt="%0.4e")
bp2 = matmul_banded( (1,1), band_a2, x2 )
print(np.allclose(bp2, b))