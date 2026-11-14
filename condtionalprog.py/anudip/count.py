f={}
a='Prachi Tyagi'
for ch in a:
    if ch in f:
        f[ch]+=1
    else:
        f[ch]=1
print(f)