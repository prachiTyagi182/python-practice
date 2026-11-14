# # shape means array ka size
# # shape=3 means one d
# # we use it when we have to save the space for the future values till now we asuming them to be zero
# import numpy as np
# default_array=np.zeros(3)
# print(default_array)#outpit=[0.0.0.] yaha 0. isliye aa rha hai kyuki by default NumPy float datatype use krta hai
# # if we want it to be in int we have to write dtype=int


# # ones jb hume array mein 1 store krta hai
# import numpy as np
# ones_array=np.ones([2,3],dtype=int)
# print(ones_array)
# print(ones_array.dtype)#output=float64 means 64 bit floating number
# # dtype hi isliye kyuki parameter ko yhi name diya hai


# # if we want ki kisi sepecfic value se hi toh we use full function
# import numpy as np
# arr=np.full([2,3],8)
# print(arr)