def lastDigit(num):
    return num%10
def isAutomorphic(num):
    if lastDigit(num) == lastDigit(num**2):
        return 1
    else:
        return 0
print("Enter a number to check whether it is Automorphic or not.\n")
number = int(input())
if(isAutomorphic(number)):
    print("Number",number, "is Automorphic")
else:
    print("Number",number, "is not Automorphic")