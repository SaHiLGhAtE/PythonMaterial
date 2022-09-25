#multiple inheritance
class Employee:
    var=7
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"The name is {self.name}.salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(string.split("-"))

    @staticmethod
    def printgood():
        print("This is good")

class Player:
    var=9
    no_of_games=4

    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The name is {self.name} and the game is {self.game}"

class Coolprogrammer(Employee,Player):
    # var=10
    language="C++"
    def printlanguage(self):
        # print(self.language)
        self.language=language
harry=Employee("Harry",1000,"Instructor")
rohan=Employee("Rohan",2000,"Student")

shubham=Player("Shubham",["Cricket"])
karan=Coolprogrammer("Karan",5000,"coolprogrammer")

# print(shubham.printdetails())
# karan.printlanguage()
# det=karan.printdetails()
# print(det)
print(karan.printdetails())
# print(karan.printlanguage())
print(karan.language)
