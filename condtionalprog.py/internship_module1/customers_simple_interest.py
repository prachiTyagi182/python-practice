class customers:
   
 def __init__(self,principal,rate,time):
      self.principal=principal
      self.rate=rate
      self.time=time


 def hello(self):
  for i in range(2):
    simple_interest=(self.principal*self.rate*self.time)/100
    print("simple interest=",simple_interest)
    print("simple interesrt of next customer")    
print("no more customers")    
 

s=customers(1000,12,3) 
s.hello()

