
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:

    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary


class Manager(Person, Employee):

    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)


manager = Manager("Aniket", 34, "E1023", 95000)

print(manager.name)
print(manager.age)
print(manager.emp_id)
print(manager.salary)

print(Manager.__mro__)




