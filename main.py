from random import randint
from os import system
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
def blackjack_res():
  system('clear')
  
  print("Welcome to blackjack!")
  print(f"Your hand: {player}, Current score: {p1_score}")
  print(f"Dealer's hand: {dealer}")
  
def draw_card():
  for i in range(2):
    player.append(cards[randint(0,12)])
  for i in range(1):
    dealer.append(cards[randint(0,12)])

def hit():
  player.append(cards[randint(0,12)])

def player_score():
  score = 0
  for i in player:
    score += i
  return score

def dealer_score():
  score = 0
  for i in dealer:
    score += i
  return score

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
blackjack_ = True
player_turn = True
while blackjack_:
  dealer = []
  player = []
  draw_card()
  while player_turn:
    
    print("Welcome to blackjack!")
    p1_score = player_score()
    d1_score = dealer_score()
    print(f"Your hand: {player}, Current score: {p1_score}")
    print(f"Dealer's hand: {dealer}")
    if p1_score == 21:
      print("Blackjack! You Win!")
      player_turn = False
    hit_ = True
    while hit_:
      blackjack_res()
      p1_hit = input("Hit or Stand? ").lower()
      if p1_hit == 'hit':
        hit()
        p1_score = player_score()
        if p1_score == 21:
          print("Blackjack! You Win!")
          hit_ = False
          
        if p1_score > 21:
          print("Bust!, You Lose!")
          hit_ = False
      else:
        hit_ = False
    player_turn = False  
  dealer_turn = True
  while dealer_turn:
    blackjack_res()
    blackjack_ = False