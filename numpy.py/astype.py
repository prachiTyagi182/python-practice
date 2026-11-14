# data type conversion
import numpy as np
arr=np.array([[[2.0,4.8],[5.7,4.6],[6.7,8.9]]])#no round off
arr_1=arr.astype(int)
print(arr_1)
print(arr_1.ndim)