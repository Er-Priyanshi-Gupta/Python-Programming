import string
import random
def reverse(sentence):
    return sentence[::-1]
def encode(sentence):
    if len(sentence)<3:
         print(reverse(sentence))
    else:
        s = list (sentence)
        l = s[0]
        s.remove(s[0])
        s.append(l)
        s1 = ""
        s1 = s1.join(s)
        alphabet = (string.ascii_lowercase + string.ascii_uppercase)
        start = ''.join((random.choice(alphabet) for i in range(3)))
        last = ''.join((random.choice(alphabet) for i in range(3)))
        sentence =  start + s1 + last
        print(sentence,end=" ")
        return sentence
def decode(sentence):
    if (len(sentence))<3:
        print(reverse(sentence))
    else:
        start = sentence[0:3]
        last = sentence[len(sentence)-3:]
        sentence = (sentence.replace(last,''))
        sentence = (sentence.replace(start,''))
        first = sentence[len(sentence)-1:]
        sentence = first + sentence
        sentence = sentence[:len(sentence)-1]
        print(sentence,end=" ")
print("Enter a string ")
userInput = input()
print("For encoding enter 1 \nFor decoding enter 2")
choice = input()
encode(userInput) if choice == "1" else decode(userInput) if choice == '2' else  print("Invalid choice")