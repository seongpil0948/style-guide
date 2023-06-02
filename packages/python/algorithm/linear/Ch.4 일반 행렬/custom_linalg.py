import numpy as np
from scipy import linalg

# only for symmetric or Hermitian matrix
def eigh(A, M=None, eigvals_only=False):
    if(A.shape[0]!=A.shape[1]):
        raise ValueError('expected square matrix')
    if M is None:
        if np.iscomplexobj(A):
            driver = linalg.get_lapack_funcs('heev', (A,))
        else:
            driver = linalg.get_lapack_funcs('syev', (A,))
        compute_v = 1
        if eigvals_only:
            compute_v = 0
        vals, vecs, info = driver(A,compute_v=compute_v)
        if info != 0:
            raise ValueError('something is wrong in eigh')
    else:
        raise NameError('Not supported')
    
    return vals, vecs