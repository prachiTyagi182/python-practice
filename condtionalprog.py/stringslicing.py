#name="prachi tyagi"
#print(name[0:5])
# yeh 0 se n-1 krta hai mtlb agr 5 likha hai toh 4 tk jayega
# indexing humesha 0 se start hoti hai but lenth 1 se start hoti hai
# name="prachi tyagi"
# len=len(name)
# print("my name has length of",len,"characters")
# print(name[0:13])
# agr hum 0 nhi lgate hai toh by default python 0 smjhta hai
name="mango"
print(name[0:-3])
# yeh negative slicing ka example hai python kya krta hai pehle likhta hai -3 ke aage len of mango joh ki hai 5 phir wph 5 ko 3 se minus krdeta hai toh 2 ans aaya toh isliye 0 se 2 tk print hoga
print(name[-1:-3])
# yeh lenth of name yaani 5-1 =4 krga then 5-3=2 toh bnega 4:2 jiska koi sense nhi baithta toh yeh length return krga as it iss
nm="Harry"
print(nm[-4:-2])