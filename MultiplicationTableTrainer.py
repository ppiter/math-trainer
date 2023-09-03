##Multiplication table from 1 to 9 trainer program 

##Importing modules

##Randomness
import random

#timestamps
import time

#Sounds (seem to use much space in the built package)
import winsound


#Preps
version = "0.100"

##Variables preps
##Create and init some variables for future use 
questionsTotal = 0
answersTotal = 0
answersCorrect = 0
timeSpent = 0
timePenalty = 0
averageTimeSpent = 0

##Init random
random.seed()

#SaiHai
inp = input("#" + str(i) + ": How much is {a} * {b}? ".format(a=a, b=b))

if inp == "q":
    answersTotal += 1

try:
    int(inp)
except:
    print("ERROR, probably you have not provided a number")
    inp = 0


print("This is the multiplication Table knowledge test v." + version)
print("Hi! Now I will ask some 14questions, and you will type the answers.")
print("Submit numeric values, or 'q' to quit")
