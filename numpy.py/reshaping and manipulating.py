# reshaping means hum array ko 1d se 2d mein krna chahte hai iwthiut changing the data then it is called reshaping
# with the help of reshaping hum no.of rowws and coliumns ko change kr skte hai but no.of elements same hi rhnge
# reshape is only possible if the dimensions match


import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_arr=arr.reshape([2,3])
print(reshaped_arr)

# reshaping never creates a copy