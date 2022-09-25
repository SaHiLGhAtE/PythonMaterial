#lambda functions or anonymous functions
# def add(a,b)
#     return a+b

# minus=lambda x,y:x-y

# def minus(x,y):
#     return x-y

# print(minus(9,4))
a=[[2,3],[4,50],[15,20]]
def a_first(a):
    return a[1]
a.sort(key=a_first)
print(a)

a=[[2,3],[4,50],[15,20]]
a.sort(key=lambda x:x[1])
print(a)

