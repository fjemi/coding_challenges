
# coding: utf-8

# In[ ]:

# r/DailyProgrammer Challenge #1 [easy]
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/


# In[ ]:

import string


# In[ ]:

# variables to store user input

username = ""
userage = ""
userhandle = ""

# dictionary to store user infor

userdictionary = {}


# In[ ]:

# function to get the user's age
# loops until a number is entered

def inputAge(message):
    while True:
        try:
            userinput = float(input(message))
        except ValueError:
            print ("Not an number! Try again.")
            print ("\n")
            continue
        else:
            return userinput
            break


# In[ ]:

# pool of characters to choose from

pool = string.ascii_letters + string.digits + "_"
        
# function to determine if reddit handle contains correct characters

def validChar(handle):
    invalidchar = False
    
    for s in handle:
        if (s not in pool):
            invalidchar = True
            
    return invalidchar


# In[ ]:

# function to get the user's name
# must be between 3-20 characters
# only characters from A-Z, a-Z, 0-9, and _

def inputHandle(message):
    while True:
        userinput = str(input(message))
        inputlength = len(userinput)
        specialchar = validChar(userinput)

        
        if (len(userinput) > 20 or len(userinput) < 3):
            print ("Your username needs to have 3-20 characters! Try again.")
            print ("\n")
        elif (specialchar is True):
            print ("Your username can on have letters, numbers, or an underscore! Try again.")
            print ("\n")
        else:
            return userinput
            break
    


# In[ ]:

# function to return the user's name, age, and reddit handle

def printinfo(name, age, handle):
    print ("\n")
    print ("Your name is %s" % (name))
    print ("You are %.1f years old" % age)
    print ("Your reddit handle is %s" % (handle))
    print ("\n")
    return


# In[ ]:

username = input("Please enter your name: ")


# In[ ]:

userage = inputAge("Please enter your age: ")


# In[ ]:

userhandle = inputHandle("Please enter you reddit handle: ")


# In[ ]:

printinfo(username, userage, userhandle)

