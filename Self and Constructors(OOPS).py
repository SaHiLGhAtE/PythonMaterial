class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"

harry=Employee("Harry",1000,"Instructor")

# harry.name="Harry"
# harry.salary=1000
# harry.role="Instructor"
#
# print(harry.printdetails())

print(harry.name,harry.salary)

