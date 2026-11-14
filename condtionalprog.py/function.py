# with the help of functions redundency reduce hoti hai
# function is created using def keyword followed by function name and then parenthesis
# function ko call krne ke liye uska name likha then parenthesis
# jitni baar function ka name likhnge utni baar function call hoga


# function calling
# def my_name():#function definition(defining a function)
#     print("prachi tyagi")

# my_name()    
# my_name()

# return tb use hota hai jb function se aayi hui value ko variable mein store krna hai

#parameter means hum function mein value input kra rhe hai parameters variables hote hai
# function kuch values input krta hai as a parameter phir work perform hota hai then return krta hai
# function to add two numbers

# def fun_name(para1,para2):
# fun_name(arg1,arg2)function calling
# def add(a, b):
#     sum=a+b
#     print(sum)
#     return sum    
# x=add(1,6)#yaha pr return ka use hua add(1,6)ki value x mein store hogyi with the help of return phir print kraya
# print(x)
# add(2,5)
# add(10,7)

# #other way
# def add(a,b,c):
#     sum=a+b+c
#     return sum
# x=add(1,2,3)    
# print(x)
# y=add(23,33,44)
# print(y)


# default parameter hen no argument is passed aur joh parameters ko value de rhi khi hai ussi ko as argument treat kre
# eg:\\parameter ke andr value right to left store hoti hai means first second parameter then first,first to second nhi
# def my_age_sum(a, b=2):
#     sum=a+b
#     print(sum)
# #     return sum
# # my_age_sum(10)

# # WRITE A function TO PRINT number/ OF CITIES
# cities=["delhi","ghaziabad","mumbai","lucknow"]
# names=["bhoomi","aadi","prachi","rahul","neeraj"]
# def len_lis(a):
#     # print(len(a))
#     return(len(a))
# x=len_lis(cities)  
# print(x)  
# y=len_lis(names)
# print(y)

# #write a function to print all the elements of list in a single line
# cities=["mumbai","ghaziabad","ranchi","lucknow"]
# def print_city(a):
#     for i in a:
#         print(i,end=" ")
# print_city(cities)


# write a function to print factorial of n
# def fact_num(num):
#     fact=1
#     for i in range(1,num+1):
#      fact=fact*i
#     print(fact)#agr print(fact)ko ek space shift krdiya towards right toh ans 1 2 6 aise milga mtlb hr step pr print hoga
# fact_num(3)    



# #function to convert usd to inr
# def convert(value):
#     indian=value*83
#     print(value, "USD","=",indian, "INR")
# convert(56)    
# convert(100)

# #function to find max of three numbers
# def max(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest",a)
#         return a
#     elif(b>a and b>c):
#         print("b is greatest",b) 
#         return b   
#     elif(c>a and c>b):
#         print("c is greatest",c)
#         return c
# max(4,3,2)        
# max(2,6,1)
# max(1,2,3)
  
#function to count the uppercase characters in a given string
# def upper(str):
#     count=0
#     for ch in str:
#         if ch.isupper():
#             count+=1
#     print(count)        
# upper("HELLO world") #agr mai bina quotes ke likhti toh python isko variable smhta string nhi#   

#function to print even numbers from a given list
# abc=[2,4,1,3,5,6,8,7,9]
# abcd=[1,4,5,89,44,66,88]
# def even(list):
#     for i in list:
#         if i%2==0:
#             print(i,end=" ")
# even(abc)            
# # even(abcd)


# #function to remove dublicated elements from the list
# list_1=["mango","apple","banana","mango","pineapple","apple"]
# def duplicate_remove(a):
#     print(list(dict.fromkeys(a)))#we will create dictionary from list item using keys.dict automatically remove krdega kyuki dict cannot have duplicate items aur phir wapas list mein convert ho jayega
#     return(list(dict.fromkeys(a)))
# duplicate_remove(list_1)   


# #function to remove dublicated element from list using for loop
# list_1=["mango","apple","banana","mango","pineapple","apple"]
# list2=["rahul","neeraj","rahul","prachi","neeraj"]
# def duplicate_remove(a):
#     list_2=[]
#     for i in a:
#         if i not in list_2:
#             list_2.append(i)
#     print(list_2)        
#     return(list_2)
# duplicate_remove(list_1)    
# duplicate_remove(list2)  

# #function to check whether a given string is palindrome or not using slicing
# str="madam"
# str2="hello"
# def reverse(a):
#     str1=a[::-1]
#     if a == str1:
#         print("palindrome")
#         return("palindrome")
#     else:
#         print("not palindrome")
#         return("not palindrome")
# reverse(str)        
# reverse(str2)
  

#   #function to find palindrome using for loop
# #   eck whether a given string is palindrome or not using slicing
# str="madam"
# str2="hello"
# def reverse(a):
#     str1=""
#     for ch in a:
#         str1=ch+str1#reverse
        
#     if a == str1:
#         print("palindrome")
#         return("palindrome")
#     else:
#         print("not palindrome")
#         return("not palindrome")
# reverse(str)        
# reverse(str2)


# #function to print square of a number
# def square(a=3):
#     print(a*a)
# square() 
# square(2)   


# #rite a function that inputs a number and print the multiplication table of thqat number
# prod=1
# def num(a):
#     # prod=1
# #     for i in range(1,11):
# #         prod=a*i
# #         print(a,"*",i,"=",prod)
# #         # return(a,"*",i,"=",prod)isme return statement for loop ke andr hai toh value 1 pr hote hi return ho jayegi baaki ki nhi hongi
# #     # return(a,"*",i,"=",prod) 
# # num(9)        
# # # print(x)


# # write a python function to print  primes less than 1000.
# # def prime():
# #     for num in range(2,100):
# #      if num>1:
# #         for i in range(2,int(num*0.5)+1):
# #             if(num%i==0):
# #                 break
# #             else:
# #                 print(num)
# # prime()                


# # write a python function to print twin primes less than 1000.if 2 consecutive odd numbers are both prime then they are twin prime
# def is_prime(num):#check if the given number is prime or not
#     if num<2:
#        return False
#     for i in range(2,num):
#         if(num%i==0): 
#            return False
        
#     return True

# def twin_prime(max_num):#twin_prime(100)program yaha se start hota hai
#    for first_num in range(2,max_num):#(2,3,4)
#      second_num=first_num+2
#     #  if(is_prime(first_num)and is_prime(second_num)):yaha function call hua is prime(2,3,4) phir woh upr wale function pr jayega jaha check krga ki prime hai ya nhi
#      print(first_num, "and", second_num)

# twin_prime(100)        
   



# # write a function to print prime factors of a number
# def prime(num_1):
#     if num_1<2:
#         return False
#     for i in range(2,num_1):
#         if(num_1%i==0):
#             return False
#     return True
# def fact(num):
#     for i in range(2,num+1):
#         if(num%i==0 and prime(i)):
#          print(i)
# fact(56)    


# #eligible to vote or not using switch case
# def my_age(age):
#     match age:
#         case 13:
#          print("not eligigble to vote")
#         case 20:
#           print("eligible to vote")
#         case 60:  
#             print("senior citizen")
#         case _:
#             print("invalid choice")    
# my_age(20)            
# my_age(70)


#eligible to vote or not using dictionary switching
def my_age(age):
    switcher={
        13:"not eligible to vote",
        20:"eligible to vote",
        60:"senior citizen"
    }
    return switcher.get(age,"invalid choice")

x=my_age(70)    
y=my_age(20)
print(y)
print(x)
