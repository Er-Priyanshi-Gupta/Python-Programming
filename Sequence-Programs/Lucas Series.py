def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
print("Enter a length of the Lucas sequence \n")
number = int(input())
for i in range(1,number+1):
    print(lucas(i), end=' ')   