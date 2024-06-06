def sod(num):
    sum = 0
    while num :
        d = num % 10
        sum = sum + d
        num//=10
    return sum
def isNiven(num):
    if num%sod(num)==0:
        return 1
    else: return 0
print("Enter a number to check whether it is Niven (Harshad) or not.\n")
number = int(input())
if(isNiven(number)):
    print("Number",number, "is Niven (Harshad)")
else:
    print("Number",number, "is not Niven (Harshad)")