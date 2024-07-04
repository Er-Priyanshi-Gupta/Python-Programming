import random
cards = []
suits = ["Spades", "Club", "Diamond", "Heart"]
ranks = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append(suit,rank)

