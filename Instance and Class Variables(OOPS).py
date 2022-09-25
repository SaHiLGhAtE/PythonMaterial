class Employee:
    no_of_leaves=8
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=1000
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=2000
rohan.role="student"

print(harry.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves=9             #u can't change this value in the class with object
print(Employee.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves=10
print(Employee.no_of_leaves)
print(rohan.__dict__)
print(Employee.__dict__)
