# .insert(array,index,value,asix)
# asix=2 dimensional-0 for rows and 1 for column
# # none for 1 d
# import numpy as np
# arr=np.array([10,20,30,40,50,60])
# print(np.insert(arr,1,55,axis=None))

import numpy as np
arr=np.array([[10,30,50],
             [70,90,80]])
print(np.insert(arr,2,100,axis=None))


# #insertion of new row
# import numpy as np
# arr=np.array([[10,30,50],
#              [70,90,80]])
# print(np.insert(arr,1,[10,111,100],axis=0))