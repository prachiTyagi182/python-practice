# strings are immutable hum aisa nhi hai ki bilkul change nhi kr skte hum upper case to lower case kr skte hai but IN PLACE change nhi kr skte
# # IN PLACE ka mtlb hota hai org str ko modify krna bina ne string ya object bnaye,means joh characters bn gye vhi rhnge direct modification not possible
# a="prachi" 
# b=a.upper()
# print(b)#directly print(a.upper()) bhi kr skte hai
# strings are immutable woh string ko change nhi krte but original string pr operations perform krte hai aur ek new string joh ki copy and editted hai usko return krga


# # rstrip function hota hai ek joh trailing characters ko remove kr skta hai trailing characters jaise !!!!!!!!!
# c="prachiiiiiiiii!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# print(c.rstrip("!","i"))
# rstrip sirf end ke characters hi remove krta hai jaise h beech mein hai toh woh nhi krga end mein hota toh krdeta
# # rstrip right to left remove krta hai i beech mein hai isliye c as it is print hoga but agr i end mein hota toh i remove ho jata
# rstrip has one disadvantage agr hum chahe ki ek sath 2 trailing characters ko remove kre toh wwoh possible nhi ek time pr ek hi ho skta hai,it ill showw type error 
d="harry!!!!!!!!!!!harry"
print(d.replace("harry","prachi"))
print(d.count("harry"))



# # split function se string list mein bn jati hai
# e="prachi 1234 prachi1234567"
# print(e.split(" "))
# f="123456456456456"
# print(f.split("4"))


# #capitalize function se string ka first character ko uppercase mein krdega but saare characters ko lower case mein yaani ki joh bhi first letter ke badd uppercae hoga usko lower case mien krdega
# name="my name is prachi tyagi"
# print(name.capitalize())


# # center joh hai woh text ko center mein align krdega center()bracket mein jitna number likhnge yeh utna space dekr usko align krdega
# name1="this is about text alignment"
# print(name1.center(40))


# # endswith return boolean value  
# name2="this is about endswith"
# print(name2.endswith("endswith"))


# # isalnum means A-Z,a-z,0-9 ke alawa kuch bhi hai toh false return krga rna true return krga it checks wwhteter the given string is alpha numeric
# name3='123pra_chi'
# print(name3.isalnum())


# # isalpha mein numbers nhi aate baaki sb isalnum ki trah hi hai
# name4="prachi"
# print(name4.isalpha())

# # isprintable returns true if all the values given within the string are printable,printable se mtlb hai jisko print kraye toh hme he ek value dilkhe but jaise \n lgaya toh yeh nhi dikhga toh yeh non printable hai
name4="this is printable\n"
# \n-non printable

print(name4.isprintable())




# # isspace()returns true if and only if string contains white spaces
# name6="     "#space ke sath kuch aur bhi hua na tb bhi false krga sirf space hona chahiye baaki kuch bhi nhi
# print(name6.isspace())




# # istitle returns true only and only wwwhen each letter of first word is capitalised
# name6="This Is A Title"
# print(name6.istitle())

# swapcase method lowercase ko uppercase mein krta hai and vice versa
name7="this is about SWApcase"
print(name7.swapcase())



# # title() tag string ko title mein krdeta hai basically hr word ke first letter ko capital krdeta hai
# name8="it will be converted into a title"
# print(name8.title())