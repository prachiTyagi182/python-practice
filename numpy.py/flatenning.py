# it is used when we want to convert multidimensional array into 1d array
# ravel()-returns a view =org arr mein modififcations
# flatten()-copy=org arr mein no modifactions

import numpy as np
p=np.array([[1,2,3],[4,5,6]])
print(p.ravel())
print(p.flatten())