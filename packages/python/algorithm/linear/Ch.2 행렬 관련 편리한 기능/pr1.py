import numpy as np


A = np.identity(20, dtype=np.float64)

np.savetxt('pr1_out1.txt', A, fmt="%0.1f")