# # random=random numbers generate krta hai 
# # random float(0-1)
# # random is a numpy module-iske andr random numbers generate krne ke bahut saare functions hote hai
# # like rand,randint,randn
# # randn=normal distribution numbers
# # choice=list ya array se random element choose krta hai
# # rand 0se1 ke beech random decimal numbers deta hai

# # import numpy as np
# # arr=np.random.rand(4)#mtlb 4 random decimal numbers mil jayenge btwn 0 and 1
# # arr_1=np.random.rand(2,3)
# # print(arr_1)
# # print(arr)

# # randint(start,stop,total numners)#one dimensional
# # randint(start,stop,(rows,coulmn))=2 dimensionl
import numpy as np
ar=np.random.randint(1,10,5)
ar1=np.random.randint(1,10,(3,4))
print(ar)
print(ar1)


# # import numpy as np
# # arr3=np.random.choice([10,20,30,40])
# # arr4=np.random.choice([12,13,14],10)
# # print(arr4)
# # print(arr3)

# # # randn=normal distribbution ke numbers deta hai negative bhi ho skte hi
# # # shuffle=array ko mix krdeta hai
# # # seed=hr baar same output,random numbers ko repeatable bnane ke liye use hota hai
# # import numpy as np
# # b=np.array([1,2,3,4,5])
# # np.random.shuffle(b)
# # print(b)

# # # seed(1) ka mtlb ek random generator ko ek starting point dena
# # # computer actually mein random no. nhi bnata formula se banata hai toh seed uss formula ka starting point decide krta hai
# import numpy as np
# np.random.seed(5)
# print(np.random.rand(5))



# # # nan-detects missing number
# # # nam to num-joh missing values detect hui hai usko kisi number se replace krna 
# # # isinf-infinte values ko detect krne ke liye
# # # nan-not a number
# # # true means nan present hai false means waha koi number hai nan is not present
# # # nan ko compare krne ke liye use nhi kr skte 


# import numpy as np
# a=np.array([1,2,3,np.nan,4,np.nan])
# print(np.isnan(a))


# # import numpy as np
# # a=np.array([1,2,3,np.nan,4,5,np.nan])
# # print(np.nan_to_num(a,nan=10))

# # np.isinfinite=check krta hai value finite hai ya nhi(nan and isinf dono ko detect krta hai)
# import numpy as np
# a=np.array([1,2,3,4,56,np.inf,np.nan])
# print(np.isfinite(a))


# # np.isinf=isme sirf np.inf detect hoga
# # import numpy as np
# # b=np.array([1,2,3,4,np.inf,6,7,8,-np.inf])
# # print(np.isinf(b))
# # print(np.nan_to_num(b,posinf=100,neginf=-100))

# import numpy as np
# a=np.array([1,2,3,4,56,np.inf,np.nan])
# print(np.isinf(a))


# # np.nanmax=array mein se maximum value deta hai nan ko igmore krke
# import numpy as np
# c=np.array([1,2,3,4,np.nan,5,6,7])#7.0
# print(np.nanmax(c))


# #np.nanmin=array mein se  minimum value deta hai nan ko igngore krkr

# c=np.array([1,2,3,4,np.nan,5,6,7])#7.0
# print(np.nanmin(c))



# # np.where()=yeh function condition check krke values replace ya select krta hai
# # np.where(condition,value_if_true,value_if_false)
# import numpy as np
# a=([1,2,3,34,np.nan,67,890,np.nan])
# print(np.where(np.isnan(a),3,a))

# # np.ma.masked_invalid()=yeh invalid values(nan and infinity )ko mask krdeta hai means unhe calculations mein include nhi krta
# import numpy as np
# a=np.array([1,2,3,4,5,67,np.nan,89,np.inf])
# m=np.ma.masked_invalid(a)
# print(m)



# # np.clip()=values ko ek range mein krdeta hai
# import numpy as np
# a=np.array([12,34,56,29,80,90,101,110])
# print(np.clip(a,34,90))
# 34 se choti values ko 32 krdega and 90 se bdi ko 90 pr in dono ke beech ki ko jaisi hai waise rhne dega yeh
# data cleamimg mein outliers control krne ke liye use hota hai