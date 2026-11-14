# np.concatenate((arr1,arr2),axis)
# axis=0 row wise stacking,vertical stacking
# axis=1 column wis estacking,horizontal stacking
# array ko tuple ki form mein pass krn hau 
import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a+b)#a+b krga add krga na ki concatenate
print(np.concatenate((a,b)))
