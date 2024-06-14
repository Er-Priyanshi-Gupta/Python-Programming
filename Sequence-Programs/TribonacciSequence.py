def tribonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
print("Enter a length of the Tribonacci sequence \n")
number = int(input())
for i in range(1,number+1):
    print(tribonacci(i), end=' ')   