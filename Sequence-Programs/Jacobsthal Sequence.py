def jacobsthal(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return jacobsthal(n-1) + 2*jacobsthal(n-2)
print("Enter a length of the  Jacobsthal sequence \n")
number = int(input())
for i in range(1,number+1):
    print(jacobsthal(i), end=' ')   