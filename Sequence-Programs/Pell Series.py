def pell(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 2*pell(n-1) + pell(n-2)
print("Enter a length of the Pell sequence \n")
number = int(input())
for i in range(1,number+1):
    print(pell(i), end=' ')   