import string
import random
userInput = input("Enter message ")
words = userInput.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
if(coding ):
    newString = []
    for word in words:
        if(len(userInput)>=3):
            start = ''.join((random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(3)))
            last = ''.join((random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(3)))
            newString.append(start + word[1:] + word[0] + last)
        else: newString.append(word[::-1])
    print(" ".join(newString))
else: 
    newString = []
    for word in words:
        if(len(word)>=3):
            Str = word[3:-3]
            Str  = Str[-1] + Str[:-1]
            newString.append(Str)
        else: newString.append(word[::-1])
    print(" ".join(newString))
    