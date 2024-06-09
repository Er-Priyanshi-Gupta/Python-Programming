from math import sqrt
def isPrime(num):
    count = 0
    for i in range(2,num+1):
        if num%i == 0:
            count+=1
    if count!=1:
        return 0
    else: return 1
print("Enter a number to check whether it is Prime or not.\n")
number = int(input())
if(isPrime(number)):
    print("Number",number, "is Prime")
else:
    print("Number",number, "is not Prime")