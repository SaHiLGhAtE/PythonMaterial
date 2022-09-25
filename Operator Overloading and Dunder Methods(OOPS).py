class Employee:
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetails(self):
        return f"The name is {self.name}. salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"The name is {self.name},salary is {self.salary} and role is {self.role}"

    def __mul__(self, other):
        return self.salary*other.salary

    def __sub__(self, other):
        return self.salary-other.salary

    def __pow__(self, power, modulo=None):
        return self.salary**power.salary

emp1=Employee("Harry",100,"Programmer")
emp2=Employee("Rohan",5,"Cleaner")
print(emp1+emp2)
print(emp1/emp2)
print(emp1)
print(repr(emp1))
print(emp1*emp2)
print(emp1**emp2)