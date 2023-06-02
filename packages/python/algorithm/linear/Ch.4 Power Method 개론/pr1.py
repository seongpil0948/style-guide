import numpy as np
from scipy import linalg

A = np.array([[6,5],[1,2]],dtype=np.float64)


# linalg.inv 사용
inv_A = linalg.inv(A)
x_old = np.array([1,0],dtype=np.float64)
mu_old = 1
# algorithm
for k in range(1,100):
    # x_new
    x_new = inv_A @ x_old
    # normalization
    x_new = x_new / linalg.norm(x_new)
    mu_new = np.vdot( x_old, x_new) / np.vdot(x_old,x_old)

    vec_error = linalg.norm(x_new-x_old)/linalg.norm(x_new)
    eigval_error = abs( (mu_new-mu_old)/mu_new )

    x_old = x_new
    mu_old = mu_new
    
    if vec_error<1.e-7 and eigval_error<1.e-8:
        break

print(k, mu_new, vec_error, eigval_error)
print()
print(x_new)
print()

# LU decomposition 사용
lu, piv = linalg.lu_factor(A)
x_old = np.array([1,0],dtype=np.float64)
mu_old = 1
# algorithm
for k in range(1,100):
    # x_new
    x_new = linalg.lu_solve( (lu,piv), x_old) #inv_A @ x_old

    # normalization
    x_new = x_new / linalg.norm(x_new)
    mu_new = np.vdot( x_old, x_new) / np.vdot(x_old,x_old)

    vec_error = linalg.norm(x_new-x_old)/linalg.norm(x_new)
    eigval_error = abs( (mu_new-mu_old)/mu_new )

    x_old = x_new
    mu_old = mu_new
    
    if vec_error<1.e-7 and eigval_error<1.e-8:
        break

print(k, mu_new, vec_error, eigval_error)
print()
print(x_new)