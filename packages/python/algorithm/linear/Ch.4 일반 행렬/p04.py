import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt

A = np.array([[0,-1],[1,0]], dtype=np.float64)

# right=True 옵션이 있으면 eigvals만 구함
eigvals, eigvecs = linalg.eig(A)

prt(eigvals, fmt="%0.5f")
print()
prt(eigvecs, fmt="%0.5f")
print()

comp1 = A @ eigvecs
comp2 = eigvecs * eigvals
print(np.allclose(comp1, comp2))

# norm 1인거 확인해보기
v1 = eigvecs[:,0]
print(np.allclose(1,linalg.norm(v1)))

# 하나의 eigenvalue와 eigenvector 비교 (첫번째 eigenvalue와 eigenvector)
l1 = eigvals[0]
print(np.allclose(A@v1, l1*v1))