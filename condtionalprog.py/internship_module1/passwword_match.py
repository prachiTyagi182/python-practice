class password_match:
    def __init__(self,password,username):
        self.password=password
        self.username=username
    def match(self):    
      if (self.username=='admin' and self.password==123456):
        print("matches")
      else:    
        print("do not match")
s1=password_match(123456,"admin")        
s1.match()