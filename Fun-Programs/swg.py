import random  
userScore = 0
computerScore = 0
runn = "1"
while(runn == "1"):
    userChoice = input("Enter your choice:\n1 for Snake\n2 for Water\n3 for Gun\n")
    Choice = ["1", "2", "3"]
    computerChoice = random.choice(Choice)
    if runn == "1":
        if userChoice == computerChoice:print("Draw")
        else:
            if computerChoice == "1" and userChoice == "2":
                print("You Win Computer Lose")
                userScore+= 1
            elif computerChoice == "2" and userChoice == "3" :
                print("You Win Computer Lose")
                userScore+= 1
            # elif computerChoice == "3" and userChoice == "2" :
            #     print("You Win Computer Lose")
            #     userScore+= 1
            else:
                print("You Lose Computer Win")
                computerScore+= 1
    runn = input("To continue enter 1")
print(f"Your score {userScore}")   
print(f"Computer score {computerScore}")      