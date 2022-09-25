"""
Iterable=__iter__() or __getitem__() The object in which these methods are defined
Iterator=__next__() The object in which this method is defined
Iteration=The process of iterate is called Iteration.

"""
def gen(n):
    for i in range(n):
        yield i

g=gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

# for i in g:
    # print(i)

h="harry"
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

for c in h:
    print(c)

