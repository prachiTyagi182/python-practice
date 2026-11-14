attempts = 3

while attempts > 0:
    u = input("Username: ")
    p = input("Password: ")
    
    if u == "admin" and p == "1234":
        print("Login Successful!")
        break  
    else:
        attempts -= 1 
        print(f"Wrong Attempts left: {attempts}")

if attempts == 0:
    print("Account Locked!")