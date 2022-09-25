#exercise 4
#pattern printing
print("Pattern printing")
num=int(input("How many rows you want to print:"))
print("Enter 1 or 0")
bool_val=input("1 for True value and 0 for False value:")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)