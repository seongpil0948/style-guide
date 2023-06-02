import numpy as np
from scipy import linalg
from skimage import io as imgio
import matplotlib.pyplot as plt

img_mat = imgio.imread('flower.jpg', as_gray=True)

m = img_mat.shape[0]
n = img_mat.shape[1]

U, s, VT = linalg.svd(img_mat)

t = 20
comp_ratio = t*(m+n+1)/(m*n)*100.0
print(comp_ratio)
A_trunc = U[:,:t] * s[:t] @ VT[:t,:]

fig = plt.figure()
plt.imshow( A_trunc, cmap='gray' )
plt.show()
fig.savefig('output.jpg')
