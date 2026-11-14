class average:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def av(self): 
        sum=0       
        for i in self.marks:
            sum=sum+i
        lent=len(self.marks)    
        avg=sum/lent
        print("the average of",self.name,"is",avg)

s1=average("prachi",[99,98,97])   
s1.av() 