# First, we will take the input:
lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
i = 1
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(1, number):
            if number%i == 0:
                print("not")
            else:
                print(number)
