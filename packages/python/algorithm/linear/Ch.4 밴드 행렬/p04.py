import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import read_banded_h, matmul_banded_eig, matmul_banded_h


# 직접 정의
'''
A_band_h = np.array([[0,0,2,2],[0,5,5,5],[1,2,3,4]],
           dtype=np.float64)
'''

# 파일에서부터 읽기
A_band_h = read_banded_h("p04_inp1.txt",2,
           dtype=np.float64, delimiter=" ", lower=False)

# full matrix 재구축을 위해서 필요 부분 가져오기
twos = A_band_h[0,2:]
fives = A_band_h[1,1:]
diagonals = A_band_h[2,:]

A_full = np.diag(diagonals) + np.diag(fives,k=1) + np.diag(twos,k=2) + np.diag(fives,k=-1) + np.diag(twos,k=-2)

# 기존 eigh는 full matrix를 써야함
eigvals_full, eigvecs_full = linalg.eigh(A_full)
print(eigvals_full)

# band 행렬을 사용 가능
eigvals_band, eigvecs_band = linalg.eig_banded( A_band_h, lower=False )
print(eigvals_band)

# Au=lambda*u 확인
print(np.allclose(A_full@eigvecs_full, eigvecs_full*eigvals_full))

# matmul_banded_eig 활용 방법, 사이즈가 커지면 느릴 수 있으니 참고, 혹시 모를 버그가 있을 경우 알려주세요.
AV = matmul_banded_eig(2, A_band_h, eigvecs_band, lower=False)
print(np.allclose(AV,eigvecs_band*eigvals_band))