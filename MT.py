##Multiplication table from 1 to 9 knowledge test program 

##Importing modules

##Randomness
import random

#timestamps
import time

#Sounds (seem to use much space in the built package)
import winsound


#Preps
version = "0.101"

##Variables preps

##Amount of questions to be asked
questionsTotal = 20

##Create and init some variables for future use 
answersTotal = 0
answersCorrect = 0
timeSpent = 0
timePenalty = 0
averageTimeSpent = 0

##Init randomq
random.seed()

#SaiHai
print("This is the multiplication Table knowledge test v." + version)
print("Hi! Now I will ask some questions, and you will type the answers.")
print("Submit numeric values, or 'q' to quit")



## TODO: Debug, 2bedeleted
##for i in range(10):
##    a = random.randrange(1, 10)
##    b = random.randrange(1, 10)
##    res = a * b
##    print("Были сгенерированы числа a={a}, b={b}, результат перемножения res={res}".format(a=a, b=b, res=res))

##Main cycle

for i in range (1, questionsTotal + 1) :
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    startTime = time.time()

    inp = input("#" + str(i) + ": How much is {a} * {b}? ".format(a=a, b=b))

    if inp == "q":
        break
    answersTotal += 1

    try:
        int(inp)
    except:
        print("ERROR, probably you have not provided a number")
        inp = 0
        continue

    endTime = time.time()

    currentIterationDuration = str(float(endTime) - float(startTime))

    ## TODO remove debug
    ##print("It taken " + currentIterationDuration + " seconds")

    timeSpent += float(currentIterationDuration)
    
    if int(inp) == a * b :
        print("Correct!!! =)")
        answersCorrect += 1
        winsound.Beep(2000, 100)
        
        
    else:
        print("Nope! =( The correct answer is " + str(a*b) + ".")
        winsound.Beep(500, 500)

    ## A devider string to distinct iterations visually
    print("")


##Fin

## ToDo add nice handling for quitting from the first question
try: averageTimeSpent = round(timeSpent / answersTotal , 2)
except:
    print("WowWow!")
    

if averageTimeSpent <= 5 : timePenalty = 0
elif averageTimeSpent >= 10 : timePenalty = 5
else: timePenalty = round(averageTimeSpent - 5)

result = 5 - (answersTotal - answersCorrect) - timePenalty 
if result < 0 : result = 0

print("You have answered " + str(answersTotal) + " times")

## ToDo add nice handling for quitting from the first question
try: print("You have " + str(answersCorrect) + " answers correct (" + str(round(answersCorrect/answersTotal*100)) + "%)")
except: print("WowWowWow!!")

print("It has taken " + str(round(timeSpent, 2)) + " seconds (" + str(averageTimeSpent) +" seconds average)")
print("Your final score is " + str(result))
if result > 3 :
    print("CONGRATULATIONS!")
    for i in range (0, 5) :
        winsound.Beep(1000 + i * 100, 200)



