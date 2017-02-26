
# coding: utf-8

# In[ ]:

#
# Simple script to generate passwords in Python
#

import random
import string


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

def inputYesNo(message):
    while True:
        userInput = input(message).upper()
        
        if (userInput.upper() == "Y" or userInput.upper() == "N"):
            # print (userInput)
            return (userInput)
            break
        else:
            print ("Not an Y or N! Try again." + "\n")
            continue


# In[ ]:

# Character types to include in the password
# Characters are not included unless user says so

charTypes = {
    'lowercase': [False, string.ascii_lowercase],
    'uppercase': [False, string.ascii_uppercase],
    'number': [False, string.digits],
    'special': [False, string.punctuation], 
}

# Pool of characters to choose from
pool = ""


# In[ ]:

charlength = inputNumber("How many characters in the password? ")


# In[ ]:

# Asks user what chars they would like to include. Loops until one is selected.

n = 0

while True:
    for char_type in charTypes:
        use = inputYesNo("Include %s characters? (Y/N) " % (char_type))
        #print ("Use %s: %s" % (char_type, use.upper()))
    
        if (use.upper() == "Y"):
            pool += charTypes[char_type][1]
            n += 1
            
    if (n == 0):
        print ("Please select as least one char type." + "\n")
    else:
        break
        


# In[ ]:

# shuffle pool

shufflepool = "".join(random.sample(pool, len(pool)))


# In[ ]:

password = ""

for i in range(0, charlength):
    i += 1
    password += random.choice(shufflepool)

print ("Your %d character password: %s" % (charlength, password))


        
        

