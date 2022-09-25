#Diamond shape problem in programming which is not a big problem for python,
# It creates confusion when you use multiple inheritance so it is suggested that not to use multiple inheritance frequently
class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    # pass
    def met(self):
        print("This is a method of class B")

class C(A):
    pass
    # def met(self):
    #     print("This is a method of class C")

class D(C,B):
    pass
    # def met(self):
    #     print("This is a method of class D")

a=A()
b=B()
c=C()
d=D()

d.met()