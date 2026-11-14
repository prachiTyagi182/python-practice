# tumhare pass 10 days ka sales data hai
# sales=[1200,1500,1100,3000,1400,1000,1300,1700,1600,2000]
# query-1total 10 days mein kitna revenue generate hua=np.sum
#avg daily sales kitni hai=np.mean
# sbse zyada sale kis din hui aur kitni hui=np.argmax and np.max
# kya sales stable hai ya bahut zyada fluctuate ho rhi ahi=np.std
# top25% day ki sales range kya hai=np.percentile
# hr din tk ka total revenue kitna ho chuka hai=np.cumsum
# extreme values ki wajah se avg disturb hogya hai typical sales btao=np.median


import numpy as np
arr=np.array([120,150,90,300,200,80,170,350])
print("total sales=",np.sum(arr))
print("average daily orders=",np.mean(arr))
avg=np.mean(arr)
data_above_avg=arr[arr>avg]
print("values above then average=",data_above_avg)
# isko bolte haiboolean indexing,filtering and conditonal selection
max_val=np.max(arr)
max_day=np.argmax(arr) +1
print("highest order=",max_val)
print("day=",max_day)
print("stability=",np.std(arr))
print("minimum threshold value=",np.percentile(arr,75))
print("cumulative orders=",np.cumsum(arr))