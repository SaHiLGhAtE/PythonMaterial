# l=10 #Global
# def function1(n):
#     l=5 #local
#     m=8
#     print(l,m)
#     print(n,"I have printed")
#
# function1("this is me")
# print(l)

# l=10
# def function1(n):
#     l=5
#     l=l+50
#     print(l)
#     print(n,"I have printed")
# function1("This is me")

# l=10
# def function1(n):
#     global l
#     l=l+50
#     print(l)
#     print(n,"I have printed")
# function1("This is me")

def harry():
    x=20
    def Rohan():
        global x
        x=88
    print("before calling Rohan()",x)
    Rohan()
    print("after calling Rohan()",x)

harry()
print(x)