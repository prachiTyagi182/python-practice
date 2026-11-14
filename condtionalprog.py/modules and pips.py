# modules basically used to borrow someone else code 
# modules are of 2 types:
# A.built in Module
# B.external module-install ith the help of pips,woh code hota hai joh logon kr through likha hota hai and they want you to use it
# whereas built in modules woh hote hai joh python mein pre installed hote hai humne unhe exxternallu install nhi krna hota hai
# modules ka use yeh hota hai ki we dont want ki hr ek code from scratch likhe 
# import time-python ka nuilt in module load load krta haifunctions related to this time are-
# time.localtime()-current time ko fetch krta hai aur usko ek struct_time object mein convert krta hai,isme hume hrs,mins,secs raw form mein milne
# time.strftime()-strinf format timr deta hai aur yeh strcut_time ko human friednly format mein convert krta hai
# time.sleep()-python ka delay function hai ,yeh program ko kuch time ke liye pause krne mein help lrta hai
import time
#  current_time=time.localtime()
#  formatted_time=time.strftime("%H:%M:%S",current_time)
#  print("current time=",formatted_time)

print("hello")
time.sleep(3)#stop of 3 seconds
print("world")



# import time isliye use kr rhe hai kyuki yeh time module python mein pehel se hi hai aur usko use kiye nina hum uske functions ko use nhi kr skte,hume python ko btana hota hai mujhe time module chahiye uske functions ko activate  krdo isliye hum import python likhte hai
# modules=python files jisme functions,variables,classes,code likha hota hai,isse hum dusri file se import krkr use krte hai
# eg:
# math module-maths releted function deta hai
# time module-time relsted functions deta hai
# random module-rendom numbers deta hai
# os module-system related kaam deta hai