n=18
number_of_guesses=1
print("no. of guesses limited to 9")
while(number_of_guesses<=9):
    n=int(input("guess the number:\n"))
    if n<=17:
        print("ur number is less")
    elif n>=19:
        print("ur number is greater")
    else:
        print("u guessed it right")
        print("no.of guesses u took to finish-",number_of_guesses)
        break
    print("no.of guesses left",9-number_of_guesses)
    number_of_guesses=number_of_guesses+1

if(number_of_guesses>9):
    print("Game Over")


