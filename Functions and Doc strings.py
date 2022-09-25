# a=9
# b=8
# c=sum((a,b))
# print(c)

def function1():
    print("hello you are in the function 1")


function1()
function1()


def function2(a, b):
    """this is a function which will calculate average and
    this function doesn't work for three numbers"""
    average = (a + b) / 2
    # print(average)
    return average


print(function2.__doc__)
v = function2(5, 7)
print(v)
