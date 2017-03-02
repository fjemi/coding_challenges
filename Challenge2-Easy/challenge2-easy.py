
# coding: utf-8

# In[1]:

# r/DailyProgrammer Challenge #2 [easy]
# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/


# In[2]:

def FMA():
    print ("This function calculates the force of an object given its acceleration and mass")
    print ("\n")

    massinput = 0.0
    accelerationinput = 0.0
    
# get the mass
    while True:
        try:
            massinput = float(input("What is the mass of the object (kg): "))
        except ValueError:
            print ("Not a number! Try again.")
            print ("\n")
            continue
        else:
            break

# get the velocity  
    while True:
        try:
            accelerationinput = float(input("What is the acceleration of the object (m/s): "))
            print ("\n")
        except ValueError:
            print ("Not a number! Try again.")
            print ("\n")
            continue
        else:
            break
    
    force = massinput * accelerationinput**2
    
    print ("The force an object accelerating at %d with a mass of %d is %.2f" % (accelerationinput, massinput, force))


# In[3]:

def Interest():
    print ("This function calculates interest given the principal, rate, and time")
    print ("\n")
    
    pinput = 0.0
    rinput = 0.0
    time = 0.0
    accrued = 0.0
    
# get the Principal
    while True:
        try:
            pinput = float(input("What is the Principal ($): ")) 
        # check if user input is a number
        except ValueError:
            print ("Not a number! Try again.")
            print ("\n")
            continue
        else:
            # check is user input is less than 0
            if (pinput < 0):
                print ("Principal cannot be negative! Try again.")
                print ("\n")
                continue
            else:
                break
                
# get rate rate                
    while True:
        try:
            rinput = float(input("What is the rate (%): ")) 
        # check if user input is a number
        except ValueError:
            print ("Not a number! Try again.")
            print ("\n")
            continue
        else:
            # check is user input is greater than 0 or less than 1
            if (rinput < 0 or rinput > 1):
                print ("Enter a rate between 0 and 1! Try again.")
                print ("\n")
                continue
            else:
                break
                
# get the time                
    while True:
        try:
            tinput = float(input("What is the time (months): ")) 
        # check if user input is a number
        except ValueError:
            print ("Not a number! Try again.")
            print ("\n")
            continue
        else:
            # check is user input is less than 0
            if (tinput < 0):
                print ("Enter a valid time in months! Try again.")
                print ("\n")
                continue
            else:
                break
                
# simple interest A = P(1 + rt)
    accrued = pinput * (1 + rinput * tinput)

    print ("The total amount accrued is %.2f " % (accrued))


# In[5]:

function = {"FMA()": "Force","Interest()":"Interest"}

print ("This is a calculator. Please choose a function.")

for key in function:
    print ("%s Function: %s" % (function[key], key))
    
print ("What function would you like to use? ")


# In[6]:

FMA()


# In[7]:

Interest()


# In[ ]:



