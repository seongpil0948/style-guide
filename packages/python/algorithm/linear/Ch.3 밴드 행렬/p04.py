import numpy as np
from scipy import linalg
from print_lecture import print_custom as prt
from custom_band import read_banded

band_a = read_banded("p04_inp1.txt", (2,1), dtype=np.float64, 
         delimiter=" ")

prt(band_a,fmt="%0.1f")