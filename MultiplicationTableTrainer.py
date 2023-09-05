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

while (True):
    # Generate random numbers
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    c = a * b
    d = random.randrange(2, 10) * random.randrange(2, 10)
    e = random.randrange(2, 10) * random.randrange(2, 10)

    if d == c:
        d = d + 2
    
    if e == c: 
        e = e + 2

    # ToDo: make a nice re-generation routine
    # ToDo: create generation of wrong answers around the correct one.


    position_list = [1, 2, 3]
    position_of_c = position_list[random.randrange(0, 3)] 
    # Debug print("position of c is: " + str(position_of_c))   
    position_list.remove(position_of_c)
    # Debug print("new list is: " + str(position_list))

    position_of_d = position_list[random.randrange(0, 2)]    
    # Debug print("position of d is: " + str(position_of_d))     
    position_list.remove(position_of_d)
    # Debug print("new list is: " + str(position_list))

    position_of_e = position_list[0]
    # Debug print("position of e is: " + str(position_of_e))     
    
    display_list = [0, 0, 0]

    display_list[position_of_c - 1] = c
    display_list[position_of_d - 1] = d
    display_list[position_of_e - 1] = e

    print(f"Сколько будет {a} умножить на {b}?")
    print(display_list)
    print(" 1 - 2 - 3")

    inp = input("Набери номер правильного ответа и нажми Enter! ")

    if inp == "q":
        break

    try:
        int(inp)
    except:
        print("Ошибка, надо ввести число от 1 до 3")
        continue
    
    if (int(inp) < 1) | (int(inp) > 3):
        print("Ошибка, надо ввести число от 1 до 3")
        continue

    if int(inp) == position_of_c:
        print("Правильно!")
        winsound.Beep(2000, 100)
    elif int(inp) == position_of_d | int(inp) == position_of_e:
        print("Неверный ответ!")
        winsound.Beep(500, 500)
    
    print("=======================")