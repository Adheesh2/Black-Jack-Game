############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###########################################################
import random
import os
from art import logo


def dealCards():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculateScore(ls):
    if sum(ls)==21 and len(ls)==2:
        return 0
    elif sum(ls)>21 and 11 in ls:
        ls.remove(11)
        ls.append(1)
    
    return sum(ls)


def compare(userScore,compScore):
    if userScore==compScore:
        return "Draw 🙃"
    elif compScore==0:
        return "Lose, opponent has Blackjack 😱"
    elif userScore==0:
        return "Win with a Blackjack 😎"
    elif userScore>21:
        return "You went over. You lose 😭"
    elif compScore>21:
        return "Opponent went over. You win 😁"
    elif userScore>compScore:
        return "You win 😃"
    else:
        return "You lose 😤"


def playGame():
    
    gameOver=False
    userCards=[]
    compCards=[]
    for _ in range(2):
        userCards.append(dealCards())
        compCards.append(dealCards())

    while not gameOver:
        userScore=calculateScore(userCards)
        compScore=calculateScore(compCards)
        os.system("cls")
        print(logo)
        print(f"Your Cards: {userCards} and your Score:{userScore}")
        print(f"Computer's Cards: {compCards[0]}")


        if userScore==0 or compScore==0 or userScore>21:
            gameOver=True
        else:
            ch=input("Type 'y' to Deal another Card or 'n' to Stay:").lower()
            if ch=="y":
                userCards.append(dealCards())
            else:
                gameOver=True
                
    while compScore!=0 and compScore<17:
        compCards.append(dealCards())
        compScore=calculateScore(compCards)
        
    os.system("cls")
    print(logo)
    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer's final hand: {compCards}, final score: {compScore}")
    print(compare(userScore,compScore))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=="y":
    os.system("cls")
    playGame()
    