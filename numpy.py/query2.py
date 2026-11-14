# # question1-random 2*3 matrix generate kro jisme numbers 1to 20 ke beech ho
# import numpy as np
# arr=np.random.randint(1,20,(2,3))
# print(arr)

# #question2=iss array mein[[10,20,30],
#                         #    [40,50,60]
#                         #    [70,80,90]]beech ki row print krao,50 and 80 access kro,iss array ka sum,mean,max find kro

# import numpy as np
# arr1=np.array([[10,20,30],
#                [40,50,60],
#                [70,80,90]])                      
# print(arr1[1,1])  
# print(arr1[1])    
# print(arr1.sum())         
# print(arr1.mean())
# print(arr1.max())
# print(arr1.ravel())
# print(arr1.flatten())

# import numpy as np
# a=np.random.randint(1,50,(3,3))
# print(a.max())
# print(a.shape)
# print(a.size)#total elements

# import numpy as np
# ar=np.array([1,2,3,4,5,6,7,8,9])
# print(ar.reshape(3,3))

# #1 to 10 tk ke numbers ka array bnao and shape print kro
# import numpy as np
# b=np.arange(1,11,1)
# print(b)
# print(b.shape)#iska output(10,)aa rha hai means 10 total number of items and comma is represnting 1d

#1 to 20 tk numbers ka array bnao and usko 4x5 matrix mein reshape kro
import numpy as np
arr=np.arange(1,21,1)
print(arr.reshape(4,5))

# random 3*4 ki matrix generate kro jisme numbers 10-15 ke beech ho
import numpy as np
arr1=np.random.randint(10,15,(3,4))
print(arr1)