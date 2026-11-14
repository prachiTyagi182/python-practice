# diff size arrays pr operation perform krna bina usko manually resize kiye
# numpy arrays ko automatically adjust krdeta hai taaki operation possible ho jaye
# eg a=[1,2,3]
#    b=2
#    a+b perform krna hai toh numpy with the help of broadcasring b ko [2,2,2]ki trah trrat krga
# aur iska result[3,4,5] aayega

# import numpy as np
# a=np.array([10,20,30])
# b=100
# print(a+b)
# broadcasting is used in =
# machine learning
# image processing
# mathematical operations on array


# import numpy as np
# arr=np.array([[10,20,30],
#              [50,60,70]])
# b=[[1],[3]]             
# print(arr+b)


# import numpy as np
# arr=np.array([[10,20,30],
#              [50,60,70]])
# arr2=np.array([[70,80,90],
#              [50,60,70]])
# print(arr+arr2)             
# sum=arr+arr2          
# print(arr+sum)

import numpy as np
arr=np.array([2,4,6,8])
b=3
print(arr+b)

import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([10,20,30])            
print(a+b)


import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([[1],[2]])
print(a*b)


import numpy as np
a=np.array([[[1,2,3],
            [4,5,6],
            [7,8,9]]])
b=np.array([10,20,30])            
print(a+b)


import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([5,10])            
print(a+b)