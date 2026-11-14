class eligible:
    def __init__(self,age):
        self.age=age
    def h(self):    
      if(self.age>6 and self.age<18):
        print("pricing will be rupees 100 for children")
      elif(self.age>18 and self.age<60):
        print("pricing will be rupees 300 for adults")    
      else:    
        print("pricing will be rupees 150 for senior citizen")


s1=eligible(20)       
s1.h()


