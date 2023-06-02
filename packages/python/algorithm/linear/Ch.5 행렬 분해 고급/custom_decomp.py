import numpy as np
def perm_from_piv(piv):
    n = np.shape(piv)[0]
    perm = np.array( range(0,n), dtype=np.int32)
    for i in range(0,n):
        # i와 piv[i]의 row가 바뀌어야함
        # swap using tuple unpacking
        perm[i], perm[piv[i]] = perm[piv[i]], perm[i]
    return perm

def LU_from_LU_band(tup, lbw ):
    # square matrix only
    LU_band = tup[0]
    piv = tup[1]
    n_row = np.shape(LU_band)[0]
    n_diag = np.shape(LU_band)[1]
    ubw = n_row - lbw -1
    U = np.zeros((n_diag,n_diag),dtype=type(LU_band[0,0]))
    for band_id in range(0,ubw+1):
        U += np.diag(LU_band[ubw-band_id,band_id:],k=band_id)
    L = np.zeros((n_diag,n_diag),dtype=type(LU_band[0,0]))
    for i in range(ubw+1,n_row):
        band_id = ubw - i
        L += np.diag(LU_band[i,:band_id],k=band_id)
    # row interchange by piv
    for i in range(0,n_diag):
        # only for lower part
        for j in range(0,i):
            # 바뀔 row, column index의 row가 항상 column 보다 커야함
            if piv[i] > j:
                L[i,j], L[piv[i],j] = L[piv[i],j], L[i,j]
    L += np.identity(n_diag)
    return L, U