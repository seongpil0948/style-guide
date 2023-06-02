import numpy as np
from scipy import linalg

A = np.array([[6,5],[1,2]],dtype=np.float64)

x_old = np.array([1,0],dtype=np.float64)
mu_old = 1
# algorithm
for k in range(1,20):
    # x_new
    x_new = A @ x_old
    # normalization
    x_new = x_new / linalg.norm(x_new)
    mu_new = np.vdot( x_new, A@x_new) / np.vdot(x_new,x_new)

    vec_error = linalg.norm(x_new-x_old)/linalg.norm(x_new)
    eigval_error = abs( (mu_new-mu_old)/mu_new )

    x_old = x_new
    mu_old = mu_new
    
    if vec_error<1.e-7 and eigval_error<1.e-8:
        break

print(k, mu_new, vec_error, eigval_error)
print()
print(x_new)