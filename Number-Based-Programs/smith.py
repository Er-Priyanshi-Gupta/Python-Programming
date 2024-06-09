from math import sqrt

def sod(num):
    if num >= 0 and num < 10:
        return num
    else:
        sod = 0
        while num > 0:
            sod += num % 10
            num //= 10
        return sod

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def factors(num):
    factor_sum = 0
    i = 2
    while num > 1:
        if num % i == 0 and is_prime(i):
            factor_sum += sod(i)
            num //= i
        else:
            i += 1
    return factor_sum

def is_smith(num):
    if is_prime(num):
        return False
    return sod(num) == factors(num)

print("Enter a number to check whether it is Smith or not.\n")
number = int(input())
if is_smith(number):
    print(f"Number {number} is Smith")
else:
    print(f"Number {number} is not Smith")
