import random
def getChoice():
    playerChoice = input("Enter your choice(rock, paper, scissors): \n")
    choice = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choice)
    choices = {"player":playerChoice, "computer":computerChoice}
    return choices
def checkWin(player, computer):
    print(f"Your choose {player}, Computer choose {computer}")
    if player == computer:
        return "Its a Tie!!"
    elif player == "rock":
        if computer == "paper":
            return "Paper covers Rock! You Lose."
        else:
            return "Rock smashes Scissors! You Win!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut Paper! You Lose."
        else:
            return "Paper covers Rock! You Win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes Scissors! You Lose."
        else:
            return "Scissors cut Paper! You Win!"
choice = getChoice()
computer = choice["computer"]
player =  choice["player"]
result = checkWin(player, computer)
print(result)
