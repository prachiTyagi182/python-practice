# match case is a replacement of switch case
# same sitch ki trah ork krta hai
# python 3.10+ mein match case introduce hua
# python <3.10 mein if-elif
# default value ya case ke liye underscore _use krnge
day=4
match day:
    case 6:
        print("saturday")
    case 7:
        print("sunday")    
    case _:
        print("it is a working day")    



# pipe character | is used when we want to use more than values in one case
x=9
match x:
    case 1|2|3|4|5:
        print("this is a working day")        
    case 6|7:
        print("this is a weekend")
    case _:
        print("default case")