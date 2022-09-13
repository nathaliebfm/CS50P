import random

cards = ["jack", "queen", "king"]

random.shuffle(cards) #Will shuffle the cards. The indentation is there so the cards are printed as a list, each one in a different line
for card in cards:
    print(card)