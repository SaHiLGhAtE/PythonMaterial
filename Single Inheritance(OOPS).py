#single inheritance
class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"the name is {self.name}.salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good"+string)


class Programmer(Employee):
    def printprog(self):
        return f"The programmer's name is {self.name}.salary is {self.salary} and the role is {self.role}.the languages are {self.languages}"

    def __init__(self,aname,asalary,arole,languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages

harry=Employee("Harry",1000,"Instructor")
rohan=Employee("Rohan",2000,"Student")

shubham=Programmer("Shubham",3000,"Programmer",["python"])
karan=Programmer("Karan",4000,"Programmer",["python","cpp"])
print(karan.printprog())
print(karan.printdetails())
