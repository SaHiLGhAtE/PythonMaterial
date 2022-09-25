class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood():
        print("This is good")
        return "Sahil"

karan=Employee.from_str("Karan-500-Student")

print(karan.salary)
print(karan.printgood())