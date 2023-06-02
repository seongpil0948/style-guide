import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import read_banded_h, matmul_banded_h

b1 = np.ones((4,),dtype=np.float64)
b2 = np.ones((5,),dtype=np.float64)

band_a1_h = read_banded_h("p10_inp1.txt", 1,
         dtype=np.complex128, delimiter=" ", lower=False)

band_a2_h = read_banded_h("p10_inp2.txt",1,
         dtype=np.float64, delimiter=" ", lower=False)

x1 = linalg.solveh_banded( band_a1_h, b1, lower=False )
x2 = linalg.solveh_banded( band_a2_h, b2, lower=False )


bp1 = matmul_banded_h( 1, band_a1_h, x1, lower=False )
print(np.allclose(bp1,b1))
print()

bp2 = matmul_banded_h( 1, band_a2_h, x2, lower=False )
print(np.allclose(bp2,b2))