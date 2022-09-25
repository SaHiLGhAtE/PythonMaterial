class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set,please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting Now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

skillf=Employee("Skill","F")
print(skillf.email)
print(type(skillf))
print(id(skillf))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))

print(inspect.isclass(skillf))
print(inspect.ismodule(skillf))
print(inspect.getmodule(skillf))
print(inspect.getdoc(skillf))