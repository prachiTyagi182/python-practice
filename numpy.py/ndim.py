# with the help of ndim we can check the number of dimensions

import numpy as np
arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[[1,2],[3,4],[5,6],[2,3]]])#3 dimesional array
print(arr_1.ndim)
print(arr_2.ndim)