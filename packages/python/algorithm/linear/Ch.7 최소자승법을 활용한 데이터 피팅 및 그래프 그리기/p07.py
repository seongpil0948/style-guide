import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

data = np.genfromtxt('p07_inp1.txt',dtype=np.float64,delimiter=',')

x = data[:,0]
y = data[:,1]

n = x.shape[0]
X = np.zeros((n,4),dtype=np.float64)
X[:,0] = 1
X[:,1] = np.exp(x)
X[:,2] = np.cos(x)
X[:,3] = np.log(x)

beta, res, rank, s = linalg.lstsq(X,y)

plt.plot(x,y,'o')
xp = np.linspace(0,3,201)
yp = beta[0] + beta[1]*np.exp(xp) + beta[2]*np.cos(xp) + beta[3]*np.log(xp)
plt.plot(xp,yp)
plt.show()
