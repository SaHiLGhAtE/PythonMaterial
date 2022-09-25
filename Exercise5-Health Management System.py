#exercise 5
#Health management system
print("Health Management System\n")
print("do u want to log or retrieve?\n")
num1=int(input("1 for log and 2 for retrieve:\n"))
str1=input("enter the name of client:\n")
print("what do u want to log diet or exercise?\n")
num2=int(input("1 for diet and 2 for exercise:\n"))
d1 = {"Harry": "chicken", "Rohan": "protein shake","Hamad":"soya"}
d2={"Harry":"pushups","Rohan":"pullups","Hamad":"stretch"}
if num2==1 and str1=="Harry":
    print(d1["Harry"])
elif num2==2 and str1=="harry":
    print(d2["Harry"])
elif num2==1 and str1=="Rohan":
    print(d1["Rohan"])
elif num2==2 and str1=="Rohan":
    print(d2["Rohan"])
elif num2==1 and str1=="Hamad":
    print(d1["Hamad"])
elif num2==2 and str1=="Hamad":
    print(d2["Hamad"])
def getdata():
    import datetime
    return datetime.datetime.now()
t=getdata()
print(t)




