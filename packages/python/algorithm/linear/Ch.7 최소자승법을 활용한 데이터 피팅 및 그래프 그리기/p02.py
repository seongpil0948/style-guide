import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

x = np.array([1,2.5,3.5,4,5,7,8.5],dtype=np.float64)
y = np.array([0.3,1.1,1.5,2.0,3.2,6.6,8.6],dtype=np.float64)

n = x.shape[0]

X = np.zeros((n,3),dtype=np.float64)
X[:,0] = 1 #np.ones((n,),dtype=np.float64)
X[:,1] = x
X[:,2] = x*x # x**2 도 동일

beta, res, rank, s = linalg.lstsq(X, y)

plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')
xp = np.linspace(0,10,200)
yp = beta[0] + beta[1]*xp + beta[2]*xp**2
plt.plot(xp,yp)
plt.show()