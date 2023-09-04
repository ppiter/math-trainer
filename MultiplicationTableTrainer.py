##Multiplication table from 1 to 9 trainer program 

##Importing modules

##Randomness
import random

#timestamps
import time

#Sounds (seem to use much space in the built package)
import winsound

#Preps
VERSION = "0.100"

##Variables preps
##Create and init some variables for future use 
""" questionsTotal = 0
answersTotal = 0
answersCorrect = 0
timeSpent = 0
timePenalty = 0
averageTimeSpent = 0 """

##Init random
random.seed()

#SaiHai

print("Hi!")

do_stop = 0

while (do_stop != 1):
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    c = a * b
    d = random.randrange(2, 100)
    e = random.randrange(2, 100)

    position_list = [1, 2, 3]
    position_of_c = position_list[random.randrange(0, 3)] 
    print("position of c is: " + str(position_of_c))   
    position_list.remove(position_of_c)
    print("new list is: " + str(position_list))

    position_of_d = position_list[random.randrange(0, 2)]    
    print("position of d is: " + str(position_of_d))     
    position_list.remove(position_of_d)
    print("new list is: " + str(position_list))

    position_of_e = position_list[0]
    print("position of e is: " + str(position_of_e))     
    
      
    print(position_of_c) 
    print(position_of_d) 
    print(position_of_e) 
    print("----------")

