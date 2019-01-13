########################################################
#
# Hammurabi
#
# From: BASIC Computer Games (1978)
#       Edited by David Ahl
#
# In this game you direct the administrator of Sumeria,
# Hammurabi, how to manage the city. The city initially
# has 1,000 acres, 100 people and 3,000 bushels of grain
# in storage.
#
# You may buy and sell land with your neighboring
# city-states for bushels of grain--the price will vary
# between 17 and 26 bushels per acre. You also must use
# grain to feed your people and as seed to plant the
# next year's crop.
#
# You will quickly find that a certain number of people
# can only tend a certain amount of land and that people
# starve if they are not fed enough. You also have the
# unexpected to contend with such as a plague, rats
# destoying stored grain, and variable harvests.
#
# You will also find that managing just the few
# resources in this game is not a trivial job over a
# period of say ten years. The crisis of population
# density rears its head very rapidly.
#
# This program was originally written in Focal at DEC;
# author unknown. David Ahl converted it to BASIC and
# added the 10-year performance accessment [sic]. If
# you wish to change any of the factors, the extensive
# remarks in the program should make modification
# farily straightforward.
#
# Note for trivia buffs: somewhere along the line an m
# was dropped out of the spelling of Hammurabi in the
# Ahl version of the computer program. This error has
# spreadh far and wide until a generation of students
# who have used this program now think that Hammurabi
# is the incorrect spelling.
#
# [Note that the above description was taken from the
#  1978 edition of the book. The original author of
#  the Focal version of this game is now known to be
#  Doug Dyment, who created the program in 1968 and
#  called it "The Sumer Game".
#
# Python port by Jeff Jetton. 
#
########################################################


import random

# You may alter this statement if you want to start
# with more or less than $100.
DEFAULT_BANKROLL = 100

# functions
def dealCardNum():
    return random.randint(0, 12)

def getCardName(n):
    cardNames = (" 2", " 3", " 4", " 5", " 6", \
                 " 7", " 8", " 9", " 10", "Jack", \
                 "Queen", "King", "Ace")
    return(cardNames[n])

def displayBankroll(b):
    if bankroll > 0:
        print("You now have %s dollars\n"%b)
    


# Display initial title and instructions
print("\n               Hamurabit")
print("Creative Computing  Morristown, New Jersey")
print("\n\n\n")
print("Try your hand at governing ancient Sumeria")
print("for a ten-year term of office.\n")



# Loop for series of multiple games
keepPlaying = True
while(keepPlaying):
    
    # Initialize bankroll at start of each game
    bankroll = DEFAULT_BANKROLL
    displayBankroll(bankroll)

    # Loop for a single round. Repeat until out of money.
    while bankroll > 0:

        # Deal out dealer cards
        print("Here are your next two cards")
        dealer1 = dealCardNum()
        # If the cards match, we re-deal 2nd card until they don't
        dealer2 = dealer1
        while dealer1 == dealer2:
            dealer2 = dealCardNum()
        # Organize the cards in order if they're not already
        if (dealer1 >= dealer2):
            (dealer1, dealer2) = (dealer2, dealer1) # Ya gotta love Python!
        # Show dealer cards to the player
        # (use card name rather than internal number)
        print(getCardName(dealer1))
        print(getCardName(dealer2) + "\n")

        # Get and handle player bet choice
        betIsValid = False
        while not betIsValid:
            currBet = int(input("\nWhat is your bet? "))
            if currBet == 0:
                betIsValid = True
                print("Chicken!!\n")
            elif currBet > bankroll:
                print("Sorry, my friend but you bet too much")
                print("You have only %s dollars to bet"%bankroll)
            else:
                # Deal player card
                betIsValid = True
                player = dealCardNum()
                print(getCardName(player) + "\n")
    
                # Did we win?
                if player > dealer1 and player < dealer2:
                    print("You win!!!")
                    bankroll += currBet
                else:
                    print("Sorry, you lose")
                    bankroll -= currBet

                # Update player on new bankroll level
                displayBankroll(bankroll)
            
    # End of loop for a single round

    print("\n\nSorry, friend but you blew your wad")
    playerResponse = input("Try again (yes or no) ")
    if playerResponse.lower() == "yes":
        print()
    else:
        keepPlaying = False

# End of multiple game loop

print("OK Hope you had fun\n")


########################################################
#
# Porting notes:
#
#   The original BASIC version had a variable named N
#   that was initialized to 100 and then never used.
#   Maybe it did something in feature that was edited
#   out of the final version used in the book?
#
#   The card value printing code was originally
#   repeated three times: Once for the two dealer
#   cards and again for the player card. This has
#   been broken out into a single, reused function.
#
#   The original program simply generated random numbers
#   for each card. It did not simulate a true card deck,
#   where the dealing of a card eliminates it from the
#   deck and reduces the chances of the same value
#   being drawn. This "infinite deck" logic (or "deal,
#   with replacement after") has NOT been changed.
#
#   Like the original program, we still allow entering
#   negative bet values, which will earn the player
#   money if they lose! :-)
#
#   The original program tracked cards as integers that
#   directly matched their values. So a deuce was 2, etc.
#   Here, cards are internally represented by integers
#   between 0 and 12. A deuce is now stored as 0, and
#   merely displayed to the player as "2". This does
#   not affect the calculation of wins/losses, but it
#   does make translating the number to text a bit
#   more straightforward.
#
#
# Ideas for Modifications
#
#   Give the user the ability to quit the game, perhaps
#   by typing "quit" instead of making a bet. Provide a
#   final assement based on how much of the original
#   bankroll they have left.
#
#   Or have the game run for a set number of rounds or
#   until a certain bankroll goal is attained.
#
#   See "porting notes" above about negative bet values.
#   In fact, other than checking to make sure the player
#   has enough in the bankroll, there is no validation
#   of bet input. Try entering a word instead of a
#   number, for example. What happens? How would you
#   fix these problems?
#
#   When the player "chickens out", show them what the
#   next card would've been and point out whether they
#   made a good or bad decision.
# 
#   Instead of calling the player "chicken" every time
#   they opt out of betting, how about random taunts?
#
#   In what situations are the odds of winning high
#   enough to justify making a bet? Create a cheat mode
#   where the program identifies these situations and
#   lets the player know.
#
#   Change the card dealing to simulate deals from a
#   single deck (or a user-selectable number of decks).
#
#   Implement a two-player mode where players take turns
#   betting (or both bet on the same dealer cards and
#   get their own player card dealt).
#
########################################################


            
        
    

    