# Public=variables which can be accessed by anyone
# Protected=variables which can be accessed by subclasses only
# private=variables which cannot be accessed by anyone except for u only

class Employee:
    no_of_leaves=10
    _protected=15
    __private=20

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

harry=Employee("Harry",1000,"programmer")
print(harry.name)
print(harry._protected)
print(harry._Employee__private)