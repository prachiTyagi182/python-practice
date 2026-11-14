import copy
class Employee:

    def __init__(self, skills):
        self.skills = skills


employee = Employee(["Python", "SQL"])

shallow = copy.copy(employee)
deep = copy.deepcopy(employee)

employee.skills.append("Machine Learning")

print(employee.skills)
print(shallow.skills)
print(deep.skills)