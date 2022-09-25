f1=open("harry.txt")

try:
    f=open("does.txt")

except Exception as e:
    print(e)

# except EOFError as e :
#     print("Eof error occured")
#
# except IOError as e:
#     print("Io error occured")

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway......")
    # f.close()
    f1.close()
print("Important stuff")