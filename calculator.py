print("Welcome to the Calculator")
print("Operations done by the calculator on two numbers are: +, -, *, /, //, **,%")
print("Enter 1 number")
num1 = int(input())
print("Enter 2 number")
num2 = int(input())
print("Enter the operation you want to perform")
operator = input()
if (operator == "+"):
    print(num1 + num2)
elif (operator == "-"):
    print(num1 - num2)
elif (operator == "/"):
    print(num1 / num2)
elif (operator == "//"):
    print(num1 // num2)
elif (operator == "*"):
    print(num1 * num2)
elif (operator == "**"):
    print(num1 ** num2)
elif (operator == "%"):
    print(num1 % num2)
else:
    print("Invalid Operator")