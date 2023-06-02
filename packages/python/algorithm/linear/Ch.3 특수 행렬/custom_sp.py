import numpy as np

def matmul_toeplitz(cr_tup,x):
    n = len(x)
    dtype = np.float64
    if type(cr_tup[0][0]) == np.complex128:
        np.complex128
    if type(cr_tup[1][0]) == np.complex128:
        np.complex128
    if type(x[0]) == np.complex128:
        np.complex128

    b = np.zeros((n,),dtype=dtype)
    for i in range(0,n):
        b[i] += np.dot(cr_tup[1][0:n-i], x[i:n])
        b[i] += np.dot(cr_tup[0][i:0:-1], x[0:i])
    return b

def matmul_circulant(c,x):
    n = len(x)
    dtype = np.float64
    if type(c[0]) == np.complex128:
        np.complex128
    if type(x[0]) == np.complex128:
        np.complex128
    cr = np.array( [c[0]] )
    idx = np.array(range(n-1,0,-1))
    cr = np.hstack( (cr, c[idx] ))
    b = np.zeros((n,),dtype=dtype)
    for i in range(0,n):
        if i==0:
            b[i] = np.dot( cr[0:n], x[0:n] )
        else:
            b[i] += np.dot(cr[i:n],x[0:n-i])
            idx = np.array(range(0,i),dtype=np.int32)
            b[i] += np.dot(cr[idx],x[n-i:n])
    return b