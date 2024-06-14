def perrin(n):
    if n == 0:
        return 3
    if n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return perrin(n-2) + perrin(n-3)
print("Enter a length of the Perrin sequence \n")
number = int(input())
for i in range(number+1):
    print(perrin(i), end=' ')   