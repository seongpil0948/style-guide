import numpy as np
from scipy import linalg

n = 20
off_diagonals = np.ones((n-1,),dtype=np.float64)
diagonals = 2*np.ones((n,),dtype=np.float64)

A_full = np.diag(diagonals)+np.diag(off_diagonals,k=1)+np.diag(off_diagonals,k=-1)

eigvals = linalg.eigh(A_full, eigvals_only = True)

x_old = np.zeros((n,),dtype=np.float64)
x_old[0] = 1
mu_old = 1
# algorithm
for k in range(1,10000):
    # x_new
    x_new = A_full @ x_old
    # normalization
    x_new = x_new / linalg.norm(x_new)
    
    mu_new = np.vdot( x_new, A_full@x_new) / np.vdot(x_new,x_new)
    

    vec_error = linalg.norm(x_new-x_old)/linalg.norm(x_new)
    eigval_error = abs( (mu_new-mu_old)/mu_new )

    x_old = x_new
    mu_old = mu_new
    
    if vec_error<1.e-5 and eigval_error<1.e-5:
        break

print("from eigh: ",eigvals[19])
print()
print("from power method: ",mu_new,k)

#print(A_full)7