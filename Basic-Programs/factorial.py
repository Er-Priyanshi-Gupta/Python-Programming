def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
print("Enter a number whose factorial you want to know\n")
number = int(input())
print(factorial(number))