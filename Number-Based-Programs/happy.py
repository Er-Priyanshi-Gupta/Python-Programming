def squareSod(num):
    d = 0 
    square = 0
    while num>0:
        d = num%10
        square = square + d**2
        num//=10
    return square
def isHappy(num):
    happy = squareSod(num)
    while 1 :
        if happy == 1:return 1
        elif happy>9:happy = squareSod(happy)
        else: return 0
        
print("Enter a number to check whether it is Happy or not.\n")
number = int(input())
if(isHappy(number)):
    print("Number",number, "is Happy")
else:
    print("Number",number, "is not Happy")