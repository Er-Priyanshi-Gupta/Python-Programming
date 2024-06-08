def square(num):
    return num**2
def isKaprekar(num):
    first = square(num)%(10**len(str(num)))
    last = square(num)//(10**len(str(num)))
    if num == first + last :
        return 1
    else:
        return 0
print("Enter a number to check whether it is Kaprekar or not.\n")
number = int(input())
if(isKaprekar(number)):
    print("Number",number, "is Kaprekar")
else:
    print("Number",number, "is not Kaprekar")  