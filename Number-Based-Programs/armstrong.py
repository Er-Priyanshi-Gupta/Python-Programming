def armstrong(num):
    length = len(str(num))
    sum = 0
    while num :
        remainder = num%10
        sum+= remainder**length
        num//=10
    return sum
def isArmstrong(n):
    if(n == armstrong(n)):
        return 1
    else:
        return 0
print("Enter a number to check whether it is Armstrong or not.\n")
number = int(input())
if(isArmstrong(number)):
    print("Number",number, "is Armstrong")
else:
    print("Number",number, "is not Armstrong")