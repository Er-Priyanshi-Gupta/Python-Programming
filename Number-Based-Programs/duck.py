def isDuck(num):
    if num[0] == '0':
        return 0
    else:
        for i in num:
            if i == '0':
                return 1
    return 0
print("Enter a number to check whether it is Duck or not.\n")
number = input()
if(isDuck(number)):
    print("Number",number, "is Duck")
else:
    print("Number",number, "is not Duck")
