def padovan(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 1
    else:
        return padovan(n-2) + padovan(n-3)
print("Enter a length of the Padovan sequence \n")
number = int(input())
for i in range(1,number+1):
    print(padovan(i), end=' ')   