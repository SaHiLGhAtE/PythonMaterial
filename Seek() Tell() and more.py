f=open("harry.txt")
print(f.tell())#To see where our pointer is
print(f.readline())
f.seek(0)#It resets the pointer again and make it 0 and whatever the value u give it will run from that location
print(f.readline())
print(f.readline())
print(f.tell())
f.close()

# f=open("harry.txt","r+")
# f.read()
# print(f.write("harry bhai bahot achhe hai\n"))
# f.close()
