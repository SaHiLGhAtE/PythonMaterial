f=open("harry.txt")
print(f.tell())
print(f.readline())
f.seek(0)
print(f.readline())
print(f.readline())
print(f.tell())
f.close()

# f=open("harry.txt","r+")
# f.read()
# print(f.write("harry bhai bahot achhe hai\n"))
# f.close()