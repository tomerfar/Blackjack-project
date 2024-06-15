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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
from art import logo
from replit import clear

def dealCards(deck, playerList, dealerList):
  playerList.append(random.choice(deck))
  playerList.append(random.choice(deck))
  dealerList.append(random.choice(deck))
  dealerList.append(random.choice(deck))

def checkWinner(pCards,pScore, dCards, dScore):
  print(f"Your final hand: {pCards}, final score: {pScore}")
  print(f"Computer's final hand: {dCards}, final score: {dScore}")
  if pScore <= 21 and pScore > dScore: #player is the winner
    if pScore == 21 and len(pCards) == 2:
      print("You win with a Blackjack :)\n")
    else:
      print("You win:)\n")

  elif pScore <= 21 and dScore > 21: #Dealer went over 21
    print("Opponent went over. You win:)\n")

  elif pScore > 21:
    print("You went over. You lose:(\n") # Player went over 21

  elif pScore < 21 and dScore < 21 and pScore < dScore: #dealer is the winner
    print("You lose\n")
  else:
    print("It's a draw!")
    
  #clear()

def dealerPlays(dScore, dealerList, deck):
  score = dScore
  while score <= 16:
    extraCard = random.choice(deck)
    dealerList.append(extraCard)
    score = sum(dealerList)
    if 11 in dealerList and score > 21:
      dealerList[dealerList.index(11)] = 1
      score = sum(dealerList)

  return score

def playerPlays(pScore,playerList, deck):
  score = pScore
  extraCard = random.choice(deck)
  playerList.append(extraCard)
  score = sum(playerList)
  if 11 in playerList and score > 21:
    playerList[playerList.index(11)] = 1
    score = sum(playerList)

  return score
  

def showScore(player_cards, player_score, dealer_cards):
  print(f"Your cards:{player_cards}, current score: {player_score} ")
  print(f"Computer's first hand: {dealer_cards[0]}")

def swapAceForOne(pScore, playerList):
  score = pScore
  playerList[playerList.index(11)] = 1
  score = sum(playerList)
  return score
  
#Main Program
want_to_play = input("Do you want to play a game of Blackjack? type 'y' or 'n':")
if want_to_play == 'y': # maybe needs to add a sequence where the user says no.
  play = True
  print(logo)
  while play:
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = [] #initializing player's cards list
    dealer_cards = [] #initializing dealer's cards list
  # Dealing cards randomly to both players
    dealCards(cards, player_cards, dealer_cards)
    player_score = player_cards[0] + player_cards[1]
    dealer_score = dealer_cards[0] + dealer_cards[1]
    #needs to deal here with a case which we get 2 aces in our hand
    #needs to deal here with a case where we get a Blackjack
    if player_score == 22:
      player_score = swapAceForOne(player_cards, player_score) # if player got 2 aces, i.e has 22
    showScore(player_cards, player_score, dealer_cards)
    if player_score == 21: # blackjack on first deal
      checkWinner(player_cards, player_score, dealer_cards, dealer_score)
      want_to_play = input("Do you want to play a game of Blackjack? type 'y' or 'n':")
      if want_to_play == 'n':
        play = False
      clear()
      print(logo)
    # here needs to start the loop again since the game is over
    else:
        keepPlay = True
        while keepPlay:
          
          cardOrStand = input("Type 'y' to get another card, type 'n' to stand:")
          if cardOrStand == "n":
            dealer_score = dealerPlays(dealer_score, dealer_cards, cards)
            #only dealer keeps playing until he has more than 16 in his hand
            checkWinner(player_cards, player_score, dealer_cards, dealer_score)
            keepPlay = False
              
          else: # player wants do draw more card
            player_score = playerPlays(player_score,player_cards,cards)
            if player_score > 21: # player loses
              keepPlay = False # will exit the inner loop
              checkWinner(player_cards, player_score, dealer_cards, dealer_score)
            else:
              showScore(player_cards, player_score, dealer_cards)
            

        want_to_play = input("Do you want to play a game of Blackjack? type 'y' or 'n':")
        if want_to_play == 'n':
          play = False
        clear()
        print(logo)
        
  
        



        
        
      
      
   
 
  
  