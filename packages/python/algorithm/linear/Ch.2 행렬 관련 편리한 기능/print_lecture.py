import numpy as np
# x는 엔트리, prc는 표시할 소수점, fmt은 'e'혹은 'f', end는 뒤에 붙일 문자
# 줄바꿈 안하고 출력 줄바꿈을 원하면 end에 '\n' 을 넣으면됨
def print_entry(x,fmt='%0.4e',end=''):
    complex_bool = False
    if type(x) == np.complex128:
        complex_bool = True
    if complex_bool:
        print( '('+'- '[x.real>=0]+fmt%abs(x.real) + \
              '+-'[x.imag<0] + fmt%abs(x.imag) + 'j'+')', end=end )
    else:
        print( '- '[x>=0] + fmt%abs(x), end=end )

# 커스텀 출력
# vector와 matrix 출력
def print_custom(x,fmt='%0.4e',delimiter=', ',line=True):
    # vector (1d array)
    vector_bool = False
    if len(x.shape) == 1:
        vector_bool = True

        
    for i in range(0,x.shape[0]):
        if vector_bool:
            if i == (x.shape[0]-1):
                print_entry(x[i],fmt=fmt, end=('','\n')[line] )
            else:
                print_entry(x[i],fmt=fmt, end=delimiter)
        if not vector_bool:
            for j in range(0,x.shape[1]):
                if j == (x.shape[1]-1):
                    print_entry(x[i,j],fmt=fmt, end=('','\n')[line])
                else:
                    print_entry(x[i,j],fmt=fmt, end=delimiter)

