# vstack=vetical row wisw,np.row_stack
# hstack=horizontal column wise
# dstack=depth stacking,yeh array ko 3rd dimension mein stack krta hai,np.column_stack(),yeh humesha axis=2 pr work krta hai automaticall
# #stack=yeh new axis create krke stack krta hai
# # np.block=yeh complex stacking kr liye use hota hai jb multiple arrays ko grid pattern mein arrange krna ho 


# import numpy as np
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print(np.hstack((arr1,arr2)))
# print(np.vstack((arr1,arr2)))
# print(np.concatenate((arr1,arr2)))
# print(np.dstack((arr1,arr2)))
# print(np.stack((arr1,arr2),axis=0))


# np.hstack=np.concatenate#both add horizontally


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.block([[arr1,arr2],[arr2,arr1]]))


# import numpy as np
# arr1=np.array([[1,2,3],
#               [4,5,6]])
# arr2=np.array([[7,8,9],
#               [10,11,12]])
# print(np.block([[arr1,arr2],[arr2,arr1]]))