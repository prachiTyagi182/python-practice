class lis:
    def __init__(self,list_1):
        self.list_1=list_1
        
        
        
    def hello(self):        #creating a lst
    #    self.list_1=['A203','A201','A890','A203','A101','A890']

# converting list to set and removing duplicate elements
       set_1=set(self.list_1)

#again converting the set to list after removing duplicates keys 
       self.list_1=list(set_1)
       print(self.list_1)
s=lis(['A203','A201','A890','A203','A101','A890'])
s.hello()