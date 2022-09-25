class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry=Employee("Harry",1000,"Instructor")
rohan=Employee("Rohan",2000,"Student")

harry.change_leaves(50)

print(harry.no_of_leaves)