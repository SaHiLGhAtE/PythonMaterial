# def print2(str1):
#     print("this is "+str1)
#
# print2("harry")

# n!=n*n-1*n-2*n-3......1
# n!=n*(n-1)!
def factorial_iterative(n):
    """:param n:Integer
       :return:n*n-1*n-2*n-3.....1
    """
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def factorial_recursive(n):
    """:param n:Integer
       :return:n*n-1*n-2*n-3.....1
    """
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
    # 5*factorial_recursive(4)
    # 5*4*factorial_recursive(3)
    # 5*4*3*factorial_recursive(2)
    # 5*4*3*2*factorial_recursive(1)
    # 5*4*3*2*1=120

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# 0,1,1,2,3,5,8
number=int(input("enter the number"))
# print("factorial using iterative method",factorial_iterative(number))
# print("factorial using recursive method",factorial_recursive(number))
print(fibonacci(number))


