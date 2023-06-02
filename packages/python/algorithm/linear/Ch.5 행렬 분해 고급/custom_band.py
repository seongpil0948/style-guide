import numpy as np
from io import StringIO
def read_banded(f_name, band_tup, dtype=np.float64, delimiter=','):
    # band_tup[0] = lower band width (양수)
    # band_tup[1] = upper band width (양수)
    # number of band matrix rows, and columns
    n_brow = (band_tup[0] + band_tup[1] + 1) 
    n_bcol = 0 # init
    with open(f_name) as f:
        lines=f.readlines()
        for row_id, line in enumerate(lines):
            #print(line,dtype)
            row = np.genfromtxt(StringIO(line), dtype=dtype, delimiter=delimiter)
            # check the size of square matrix
            if row_id == 0:
                n = len(row)
                n_bcol = n
                # band matrix shapes
                a = np.zeros((n_brow,n_bcol),dtype=dtype)
            # row_id = diagonal index
            #print(row_id,row)
            # row내에서 read
            row_min = row_id - band_tup[0]
            row_max = row_id + band_tup[1]
            if row_min < 0:
                row_min = 0
            if row_max >= n:
                row_max = n-1
            #print(row_min,row_max)
            for col_id in range(row_min,row_max+1):
                band_row_id = row_id - col_id + band_tup[1]
                #print(band_row_id)
                a[band_row_id,col_id] = row[col_id]
            # delete temporary array
            del row
    return a

def read_banded_h(f_name, upper_width, dtype=np.float64, delimiter=',', lower=False):
    # band_tup[0] = lower band width (양수)
    # band_tup[1] = upper band width (양수)
    # number of band matrix rows, and columns
    n_brow = upper_width + 1
    n_bcol = 0 # init
    with open(f_name) as f:
        lines=f.readlines()
        for row_id, line in enumerate(lines):
            #print(line,dtype)
            row = np.genfromtxt(StringIO(line), dtype=dtype, delimiter=delimiter)
            # check the size of square matrix
            if row_id == 0:
                n = len(row)
                n_bcol = n
                # band matrix shapes
                a = np.zeros((n_brow,n_bcol),dtype=dtype)
            # row_id = diagonal index
            #print(row_id,row)
            # row내에서 read
            row_min = row_id #- band_tup[0]
            row_max = row_id + upper_width
            if row_min < 0:
                row_min = 0
            if row_max >= n:
                row_max = n-1
            #print(row_min,row_max)
            for col_id in range(row_min,row_max+1):
                band_row_id = row_id - col_id + upper_width
                if lower == True:
                    band_row_id = n_brow-1-band_row_id
                    if dtype == np.complex128:
                        a[band_row_id,col_id-band_row_id] = row[col_id].conjugate()
                    else:
                        a[band_row_id,col_id-band_row_id] = row[col_id]
                else:
                    a[band_row_id,col_id] = row[col_id]
            # delete temporary array
            del row
    return a
"""
def matmul_banded(band_tup,band_a,x):
    dtype = np.float64
    if type(band_a[0,0])==np.complex128:
        dtype = np.complex128
    if type(x[0])==np.complex128:
        dtype = np.complex128
    band_nrow = band_a.shape[0]
    n = band_a.shape[1]
    if n != len(x):
        raise NameError('size is not proper in "matmul_band"')
    
    # initialization
    ref_band_id = band_tup[1]
    #print(ref_band_id)
    b = np.zeros((n,),dtype=dtype)
    for i in range(0,n):
        #b[i] = 0 #band_a[ref_band_id,i]*x[i]
        for j in range(-band_tup[0],band_tup[1]+1):
            # avoid bound error
            try:
                b[i] += band_a[ref_band_id-j,i+j]*x[i+j]
            except:
                b[i] = b[i]
            #if ref_band_id-j>=0 and ref_band_id-j<band_nrow:
            #    if i+j>=0 and i+j<n:
            #        #print('noerror',ref_band_id-j,i+j)
            #        b[i] += band_a[ref_band_id-j,i+j]*x[i+j]
    return b

"""
def matmul_banded(band_tup,band_a,x):
    dtype = np.float64
    if type(band_a[0,0])==np.complex128:
        dtype = np.complex128
    if type(x[0])==np.complex128:
        dtype = np.complex128
    band_nrow = band_a.shape[0]
    n = band_a.shape[1]
    if n != len(x):
        raise NameError('size is not proper in "matmul_band"')
    
    a1 = band_a*x
    upper_width = band_tup[1]

    b = np.zeros((n,),dtype=dtype)
    b[:] = a1[upper_width,:]
    for i in range(0,upper_width):
        cnt = i+1
        for j in range(0,n-i-1):
            b[j] += a1[upper_width-i-1,j+cnt]
    for i in range(upper_width+1,band_nrow):
        cnt = i-upper_width
        for j in range(i-upper_width,n):
            b[j] += a1[i,j-cnt]

    return b

"""
def matmul_banded_h(upper_width,band_a,x,lower=False):
    dtype = np.float64
    if type(band_a[0,0])==np.complex128:
        dtype = np.complex128
    if type(x[0])==np.complex128:
        dtype = np.complex128
    band_nrow = band_a.shape[0]
    n = band_a.shape[1]
    if n != len(x):
        raise NameError('size is not proper in "matmul_band"')
    # if complex, then conjugate
    # initialization
    ref_band_id = upper_width
    #print(ref_band_id)
    b = np.zeros((n,),dtype=dtype)
    for i in range(0,n):
        for j in range(0,upper_width+1):
            #print(j)
            # avoid bound error
            try:
                if lower==True:
                    b[i] += band_a[j,i].conjugate()*x[i+j]
                else:
                    b[i] += band_a[ref_band_id-j,i+j]*x[i+j]
            except:
                b[i] = b[i]
            if j != 0:
                #print(n)
                #print(i,n-i-1,j,i+j,n-i-j-1)
                #print(ref_band_id-j,i+j)
                try:
                    if lower==True:
                        # conjugate
                        b[i+j] += band_a[j,i]*x[i]
                    else:
                        # conjugate
                        b[i+j] += band_a[ref_band_id-j,i+j].conjugate()*x[i]
                except:
                    b[i] = b[i]
        
        '''
        for j in range(-upper_width,0):
            for j in range(0,upper_width+1):
                try:
                    b[i] += band_a[ref_band_id-j,i+j]*x[i+j]
                except:
                    b[i] = b[i]
        '''
    return b
"""
def matmul_banded_h(upper_width,band_a,x,lower=False):
    dtype = np.float64
    if type(band_a[0,0])==np.complex128:
        dtype = np.complex128
    if type(x[0])==np.complex128:
        dtype = np.complex128
    band_nrow = band_a.shape[0]
    n = band_a.shape[1]
    if n != len(x):
        raise NameError('size is not proper in "matmul_band"')
    # if complex, then conjugate
    # initialization
    ref_band_id = upper_width
    #print(ref_band_id)
    b = np.zeros((n,),dtype=dtype)
    # band row
    a1 = band_a * x
    #a2 = band_a[0:upper_width].conjugate()*x
    lower_band = np.zeros((upper_width,n),dtype=dtype)
    for j in range(0,upper_width):
        lower_band[upper_width-j-1,0:n+j-upper_width] = band_a[j,upper_width-j:n].conjugate()
    #print(lower_band)
    a2 = lower_band * x
    b[:] = a1[upper_width,:]
    for i in range(0,upper_width):
        cnt = i+1
        for j in range(0,n-i-1):
            b[j] += a1[upper_width-i-1,j+cnt]
        for j in range(i+1,n):
            b[j] += a2[i,j-cnt]
        """
        for j in range(0,n):
            try:
                b[j] += a1[upper_width-i-1,j+1]
            except:
                b[j] = b[j]
            try:
                b[j] += a2[i,j-1]
            except:
                b[j] = b[j]
        """
    #for i in range(0,n):
    #    b[i] = sum(a1[:,i])+sum(a2[:,i])
    return b

def matmul_banded_eig(upper_width,band_a,M,lower=False):
    cmplx = False
    if np.iscomplexobj(band_a):
        cmplx = True
    if np.iscomplexobj(M):
        cmplx = True
    dtype = np.float64
    if cmplx:
        dtype = np.complex128
    result = np.zeros((M.shape[0],M.shape[1]),dtype=dtype)
    # column vecs
    for i in range(0,M.shape[1]):
        x = M[:,i]
        result[:,i] = matmul_banded_h(upper_width,band_a,x,lower)
   
    return result
