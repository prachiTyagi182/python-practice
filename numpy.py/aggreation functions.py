# # aggreation=summarizing Data
# outlier means aisa data point joh baaki saari values se bahuyt alg ho,eg sal sbki alg alg hoti hai kisi ki 1500 toh kisi ki lakh mein toh mean se zyada meidan better hoga
# outlier is a datapoint that signigaicatly differs from other observations in dataset

# np.sum
# np.prod=probability calculations mein
# np.mean
# np.min
# np.max
# np.var
# np.std=consistency and stability ke liyen,sales stable hai ya nhi risk analysis
# index based aggreation
# np.argmax-max value ka index btata hai use=top selling day ka position nikallana
# np.argmin-min value ka index nikalna use=lowest selling day ka position nikalana

# 9 and 10 cumulative aggreation
# np.cumprod running multiplication,hr step ka multiplicayion store hota hai
# np.cumsum stock market mein cumulative returns is date tk kitna kmaya yaani ki company ne 15 days mein kitna kkmaya ,month ke beech ka reveneue

# argmax se nikala ki 5th day mein sbse zyada sale hui aur kitni sale hui woh max se
# 13 and 14 conditional aggreation
# np.any=kya koi element ture hai used in condition checking data set
# np.all=kya saare element true hai used in condition checking in dataset

# np.median=outliers case mein imp,agr data mein extreme values ho toh mean se xyada better hai median
# np.percentile=kitna percent data is value se neeche hai,top25%days mein kitni sale hoti hui
# np.percentile(arr,75)means oh value jiske neeche 75% sales aati hai
# bottom 10%=10
# top10%=90
# top n%=100-n
# np.quantile like percentile but in 0-1 range
# # import numpy as np
# arr=np.array([1,2,3])
# print(np.sum(arr))


# import numpy as np
# arr_1=np.array([[1,2,3],[10,20,30],[45,67,89]])
# print(np.max(arr_1))
# print(arr_1.ndim)



# import numpy as np
# arr_1=np.array([[[1,2,3],[10,20,30],[45,67,89]]])
# print(np.mean(arr_1))
# print(arr_1.ndim)



import numpy as np
arr_1=np.array([[1,2,3],[10,20,30],[45,67,89]])
print(np.max(arr_1))
print(np.var(arr_1))
print(np.std(arr_1))
print(arr_1.ndim)
print(arr_1.shape)
print(arr_1.size)