class myset:
  def __init__(self):
   pass
   self.items=[]
  def add (self,value):
    if value not in self.items:
      self.items.append(value)
    else:
      print(f"{value} is already there,duplicates not allowed")  
new_set=CustomSet()
new_set.add(10)      
new_set.add(5)
new_set.add(10)

print(new_set.items)

  
   


    
     