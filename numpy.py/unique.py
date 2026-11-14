# # how to find unique element of an array
# # np.unique()
# import numpy as np
# a=np.array([1,2,3,44,5,6,7,1,2,3,44])
# print(np.unique(a))

# import numpy as np
# b=np.random.randint(1,10,5)
# print(np.unique(b))
# print(b)

# import numpy as np
# abc=np.array([[[1,2,3],
#               [4,5,6],
#               [7,8,9]]])
# print(abc.shape)  
# print(abc[0])            
# print(abc[:2,:2,:2])
# means first 2 floors select kro phir hr floor se first 2 rows aur phi hr row se first 2 columns

# get the first 4 numbers of array toh isme slicing ki help se krnge


import numpy as np
abcd=np.array([23,45,6])
ab=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(abcd+ab)             