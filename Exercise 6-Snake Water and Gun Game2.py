# Exercise 6
# Snake Water and Gun

import random
lst=["s","w","g"]

chance=10
no_of_chance=0
computer_point=0
human_point=0

print("\t\t\t Snake,Water,Gun Game\n\n")
print("s for snake\nw for water\ng for gun\n")
while no_of_chance<chance:
    _input=input("Snake,Water,Gun")
    _random=random.choice(lst)

    if _input==_random:
        print("This is tie both will get 0 point\n")

    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input=="s" and _random=="w":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input=="w" and _random=="s":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input=="w" and _random=="g":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input=="g" and _random=="w":
        computer_point=computer_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("computer wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input=="g" and _random=="s":
        human_point=human_point+1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("human wins 1 point\n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    else:
        print("you entered wrong input\n")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

print("Game Over")

if computer_point==human_point:
    print("Tie")
elif computer_point>human_point:
    print("computer wins and you lose")
else:
    print("human wins and computer lose")

print(f"your points are {human_point} and computer points are {computer_point}")




