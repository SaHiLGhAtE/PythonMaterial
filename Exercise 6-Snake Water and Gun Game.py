#Exercise 6
#Snake,Water and Gun
import random
print("Snake,Water and Gun")
print("No. of guesses limited to 10")


class Snake:
    pass


S=Snake


class Water:
    pass


W=Water


class Gun:
    pass


G=Gun
str1=input("enter Snake or Water or Gun")
lst=["Snake","Water","Gun"]
choice=random.choice(lst)
number_of_attempts=1
while(number_of_attempts<=10):
    if str1=="Snake" and choice=="Water":
        print("u won")
    elif str1=="Snake" and choice=="Gun":
        print("u lose")
    elif str1=="Water" and choice=="Snake":
        print("u lose")
    elif str1=="Water" and choice=="Gun":
        print("u won")
    elif str1=="Gun" and choice=="Snake":
        print("u won")
    elif str1=="Gun" and choice=="Water":
        print("u lose")
    else:
        print("u entered something different")
        break
    print("number of attempts left",10-number_of_attempts)
    number_of_attempts=number_of_attempts+1

if(number_of_attempts>10):
    print("game over")