class bonus:
    def __init__(self,attendance_percentage,performance_rating):
        self.attendance_percentage=attendance_percentage
        self.performance_rating=performance_rating
    def fun(self):   
      if self.attendance_percentage>70 and self.performance_rating>3:
        print("eligible for bonus")
      else:
        print("not eligible for bonus")    

s=bonus(86,7)        
s.fun()
