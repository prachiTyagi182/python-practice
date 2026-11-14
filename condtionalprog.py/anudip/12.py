

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


s1 = Student("Arjun", 88)
s2 = Student("Priya", 95)

s1.display()
s2.display()