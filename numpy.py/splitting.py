import numpy as np
arr=np.array([10,20,30,40,50,60])
print(np.split(arr,3))#3 parts mein split,equal part splitting,agr splitting possible nhi toh value error aayega

import numpy as np
arr=np.array([[10,20,30],
             [40,50,60]])
print(np.hsplit(arr,3))



import numpy as np
arr=np.array([[[10,20,30],
             [40,50,60],
             [70,80,90]]])
print(np.dsplit(arr,3))