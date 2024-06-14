def tetranacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 0
    elif n == 4:
        return 1
    else:
        return tetranacci(n-1) + tetranacci(n-2) + tetranacci(n-3) + tetranacci(n-4)
print("Enter a length of the Tetranacci sequence \n")
number = int(input())
for i in range(1,number+1):
    print(tetranacci(i), end=' ')   