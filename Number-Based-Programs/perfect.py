def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)


def factorSum(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum+=i
    return sum

def isPerfect(num):
    if (num == factorSum(num)):
        return True
    else:
        return False
    
print("Enter a number to check whether it is Perfect or not.\n")
number = int(input())
if(isPerfect(number)):
    print("Number",number, "is Perfect")
else:
    print("Number",number, "is not Perfect")