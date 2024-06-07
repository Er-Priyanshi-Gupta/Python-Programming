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