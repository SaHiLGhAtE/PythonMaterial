#exercise 5
#Health management system
print("Health Management System\n")
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food"))
        if (c==1):
            value=input("Type here\n")
            with open("Harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif (c==2):
            value=input("Type here\n")
            with open("Harry-food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c==1):
            value = input("Type here\n")
            with open("Rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("Type here\n")
            with open("Rohan-food.txt", "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if (c==1):
            value = input("Type here\n")
            with open("Hamad-ex.txt", "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif (c==2):
            value = input("Type here\n")
            with open("Hamad-food.txt", "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    else:
        print("Plz enter valid input(1(Harry),2(Rohan),3(Hamad)")

def retrieve(k):
        if k==1:
            c=int(input("Enter 1 for exercise and 2 for food"))
            if(c==1):
                with open("Harry-ex.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("Harry-food.txt") as op:
                    for i in op:
                        print(i,end="")
        elif k==2:
            c=int(input("Enter 1 for exercise and 2 for food"))
            if(c==1):
                with open("Rohan-ex.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("Rohan-food.txt") as op:
                    for i in op:
                        print(i,end="")
        elif k==3:
            c=int(input("Enter 1 for exercise and 2 for food"))
            if(c==1):
                with open("Hamad-ex.txt") as op:
                    for i in op:
                        print(i,end="")
            elif(c==2):
                with open("Hamad-food.txt") as op:
                    for i in op:
                        print(i,end="")
        else:
            print("Plz enter valid input(Harry,Rohan,Hamad)")
a=int(input("Press 1 for log the value and 2 for retrieve"))

if a==1:
    b=int(input("press 1 for harry 2 for rohan and 3 for hamad"))
    take(b)
else:
    b=int(input("press 1 for harry 2 for rohan and 3 for hamad"))
    retrieve(b)










