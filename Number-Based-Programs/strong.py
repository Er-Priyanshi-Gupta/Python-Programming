def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
def sod(num):
    sum = 0
    while num :
        d = num%10
        sum = sum+factorial(d)
        num//=10
    return sum
def isStrong(num):
    if(num == sod(num)):
        print(sod(num))
        return 1
    else:
        return 0
print("Enter a number to check whether it is Strong or not.\n")
number = int(input())
if(isStrong(number)):
    print("Number",number, "is Strong")
else:
    print("Number",number, "is not Strong")
    