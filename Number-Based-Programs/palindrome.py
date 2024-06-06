def reverse(num):
    rev = 0
    while num :
        remainder = num%10
        rev = (rev*10) + remainder
        num//=10
    return rev
def ispalindrome(n):
    if(n == reverse(n)):
        return 1
    else:
        return 0
print("Enter a number to check whether it is Palindrome or not.\n")
number = int(input())
if(ispalindrome(number)):
    print("Number",number, "is Palindrome")
else:
    print("Number",number, "is not Palindrome")