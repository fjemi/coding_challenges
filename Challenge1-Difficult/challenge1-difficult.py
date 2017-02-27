
# coding: utf-8

# In[ ]:

# r/DailyProgrammer Challenge #1 - Guessing Game (difficult)
# https://www.reddit.com/r/dailyprogrammer/comments/pii6j/difficult_challenge_1/


# In[ ]:

import string
import random


# In[ ]:

# Asks the user to input a number. Loops until one is entered

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print ("Not an integer! Try again")
            continue
        else:
            return userInput
            break


# In[ ]:

# Asks the user to input a char. Loops until one is entered

def inputHiLow(message):
    while True:
        userInput = input(message).upper()
        
        if (userInput.upper() == "H" or userInput.upper() == "L"):
            # print (userInput)
            return (userInput)
            break
        else:
            print ("Not an H or L! Try again." + "\n")
            continue


# In[ ]:

# Asks the user to enter a number between 1 and 100

while True:
    usernumber = inputNumber("Enter a number between 1 and 100: ")
    if (usernumber > 0 and usernumber < 101):
        break
    else:
        print("This number is not in the range 1-100! Try again." + "\n")


# In[ ]:

# Computer picks a number
numberguesses = 1
highnumber = 101
lownumber = 0


# In[ ]:

# Computer asks if it picked the right number. Keeps guessing until it does.

while True: 
    print("\n")
    print("%d, %d" % (lownumber, highnumber))
    print("\n")
    
    computerguess = random.randint(lownumber, highnumber)
    
    print ("The computer guessed %d on try number %d " % (computerguess, numberguesses))
    print("\n")
    
    if (computerguess == usernumber): 
        print ("Your number was %d, and the computer guessed it after %d tries " % (usernumber, numberguesses)) 
        break 
    else: 
        numberguesses += 1 
        ask = inputHiLow("Is your number higher or lower than %d? [H/L] " % computerguess).upper()
        
        if (ask == "H"):
            lownumber = computerguess
        else:
            highnumber = computerguess

        


# In[ ]:



