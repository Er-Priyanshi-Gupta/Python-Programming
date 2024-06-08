from math import sqrt
def sqrtNumber(num):
    return sqrt(num)
def square(num):
    return sqrtNumber(num)**2
def isSquare(num):
    if num == square(num):
        return 1
    else: return 0
print("Enter a number to check whether it is Square or not.\n")
number = int(input())
if(isSquare(number)):
    print("Number",number, "is Square")
else:
    print("Number",number, "is not Square")