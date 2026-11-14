class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks=marks
        

    def get_grade(self):
        self.total = sum(self.marks)
        self.per = (self.total / 500) * 100
        if self.per >= 80: 
            print( "A")
        elif self.per >= 60:
            print ("B")
        elif self.per >= 40:
            print ("C")
        else:
            print ("Fail")


s=Student('prachi',[89,100,99,89,97])
s.get_grade()