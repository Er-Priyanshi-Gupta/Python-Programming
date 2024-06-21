name = input("Enter your name\n")
age = int(input("Enter your age\n"))
if age>=18:
    print(f"{name} is an adult and can vote")
else:
    print(f"{name} is not an adult and cannot vote")