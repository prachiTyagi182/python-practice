class sales:
    def __init__(self,sales_1,sales_2,sales_3):
        self.sales_1=sales_1
        self.sales_2=sales_2
        self.sales_3=sales_3


#checking conditions
    def hello(self) :
      if (self.sales_1>self.sales_2 and self.sales_1>self.sales_3):
         print("first sale figure is greatest",self.sales_1)
      elif(self.sales_2>self.sales_3 and self.sales_2>self.sales_1):
        print("second sale figure is greatest",self.sales_2)    
      else:
        print("third sale figure is greatest",self.sales_3)   


s1=sales(100,123,150)     
s1.hello()