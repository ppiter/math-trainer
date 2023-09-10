##Multiplication table from 1 to 9 trainer program 

##Importing modules

##Randomness
import random

#timestamps
import time

#Sounds (seem to use much space in the built package)
import winsound

#Preps
VERSION = "0.102"

def make_sound(type: bool, iterations, length):
    if type: frequency = 2000
    else: frequency = 500
    for i in range(iterations):
        winsound.Beep(frequency, length)
        time.sleep(0.1/1000)

##Variables preps
##Create and init some variables for future use 
total_questions = 0
correct_answers = 0
winning_streak = 0
loosing_streak = 0

##Init random
random.seed()

#SaiHai

print(f"Hi! This is multiplication table console interactive trainer v{VERSION}")

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

    total_questions += 1
    print(f"Сколько будет {a} умножить на {b}?")
    print(display_list)
    print(" 1 - 2 - 3")

    inp = input("Набери номер правильного ответа и нажми Enter. Набери q и нажми Enter для выхода.")

    if inp == "q":
        print(f"Спасибо за игру! Я задал тебе {total_questions - 1} вопросов, правильных ответов было {correct_answers}!")
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
        correct_answers += 1
        winning_streak += 1
        loosing_streak = 0
        print(f"Правильно! {a} умножить на {b} будет {c}. Это {winning_streak} правильный ответ подряд!")
        make_sound(True, winning_streak, 50)
    elif (int(inp) == position_of_d) | (int(inp) == position_of_e):
        winning_streak = 0
        loosing_streak += 1
        print(f"Неверный ответ! {a} умножить на {b} будет {c}. Это {winning_streak} неправильный ответ подряд!")
        make_sound(False, loosing_streak, 50)
    else: 
        print("Что-то пошло не так!")
        winning_streak = 0
        loosing_streak = 0

    print("=======================")