class occ:
    def __init__(self,str):
       self.str=str

    def hello(self):    
     dict={}
     
     for x in (self.str):
        if x in dict:
          dict[x]+=1
        else:
          dict[x]=1
     print(dict)        
s=occ("Prachi Tyagi")
s.hello()