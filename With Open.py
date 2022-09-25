with open("harry.txt") as f:
    a=f.readlines()
    print(a)
f=open("harry.txt")
print(f.readline())
f.close()