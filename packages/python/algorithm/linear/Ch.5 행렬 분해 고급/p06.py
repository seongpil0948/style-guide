import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_decomp import LU_from_LU_band, perm_from_piv

lbw = 2
ubw = 1

A_band = np.array([[0,2,2,2,1],[1,1,1,1,1],[1,1,1,1,0],[2,2,2,0,0]]
        ,dtype=np.float64)
dummy_array = np.zeros( (lbw, A_band.shape[1]), dtype=np.float64 )

A_band_LU = np.vstack( (dummy_array, A_band) )

gbtrf = linalg.get_lapack_funcs("gbtrf", dtype=np.float64)
LU_band, piv, info = gbtrf( A_band_LU, lbw, ubw )
print("info: ",info) # 뭔가 제대로 안돌아갈때는 info를 꼭 확인해주세요!

L, U = LU_from_LU_band( (LU_band, piv), lbw )

perm = perm_from_piv(piv)
P = np.identity(5)[perm,:]
prt(P.T@L@U, fmt="%0.0f")
