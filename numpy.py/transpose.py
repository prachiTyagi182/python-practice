# switches rows and columns
import numpy as np
a=np.array([[1,2,8,3],
           [4,5,7,6]])
print(a.T)  #shape=(4 rows,2 columns)
print(np.dstack(a))#shape = 3 dimensionala (1,4,2) where 1 is depth         