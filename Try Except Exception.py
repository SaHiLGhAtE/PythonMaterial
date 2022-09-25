print("Enter first number")
num1 = input()
print("Enter second number")
num2 = input()
try:
    print("this is the sum of two numbers", int(num1) + int(num2))
except Exception as a:
    print(a)

print("this line is very important")
