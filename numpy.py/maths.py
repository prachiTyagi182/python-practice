# # import numpy as np
# # arr=np.array([10,20,30])
# # print(arr +3)
# # print(arr -10)
# # print(arr *2)

# import numpy as np
# arr=np.array([10,20,30])
# arr[1]=arr[1]+5
# print(arr)


# import numpy as np
# arr=np.array([10,20,30])
# arr[[0,1]]=arr[[0,1]]+5
# print(arr)

# # element which is greater than 20 add 5 in it

# import numpy as np
# arr=np.array([10,20,30])
# arr[arr>20]+=5
# print(arr)

# #add 2 in only even numbers

# import numpy as np
# arr=np.array([11,20,30])
# arr[arr%2==0]+=2
# print(arr)




import numpy as np
arr=np.array([[10,20,30],
             [22,33,44]])
arr[1,1]+=5
print(arr)