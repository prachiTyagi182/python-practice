k=4
for i in range(4,0,-1):
    for j in range(1,5):
        if j==k:
            print(i,end=" ")
        else:
            print("0",end=" ")    
    k=k-1        
    print()        
