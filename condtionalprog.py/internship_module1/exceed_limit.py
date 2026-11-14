class hello:
    def __init__(self,limit):
        self.limit=limit
    def exceed(self):    
      if self.limit>60:
        print("speed limit is exceeded")
      else:
        print("speed limit is not exceeded")

s1=hello(70)        
s1.exceed()
