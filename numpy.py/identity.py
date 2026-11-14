# for identity matrix we use eye(shape)function
# np.eyee basically i=j pr 1 print krta hai baaki pe 0
# np.eye()never accepts list
import numpy as np

identity_matrix=np.eye(2,3,dtype=int)
print(identity_matrix)

#np.identity is only for square matrix so when we will write np.identity(3)it will treat as 3*3

import numpy as np
arr_1=np.identity(4,dtype=int)
print(arr_1)