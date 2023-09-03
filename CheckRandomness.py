## Check randomness of the standard random library 

## Imports
import random
import numpy
import time

## Setup
version = "0.100"
randomNumbersAmount = 10000000
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

timeStart = time.time()
for i in range (0, randomNumbersAmount):
    x = random.randrange(1,11)
    result[x-1] += 1
    ##print("I am going to increase " + str(x) + " into the field " + str(x-1))
    ##print("Current array is: " + str(result))
timeEnd = time.time()

## Calculate some statistics
timeSpent = round(timeEnd - timeStart)
performance = round(randomNumbersAmount / timeSpent) 
resultMax = numpy.max(result)
resultMin = numpy.min(result)
resultDiff = resultMax - resultMin
resultVarToSizeRatio = resultDiff / randomNumbersAmount 

## Show the result
print("There were " + str(randomNumbersAmount) + " iterations, taken " + str(timeSpent) + " seconds (" + str(performance) + " npS).")
print("Resulting array is " + str(result) + ".")
print("Max " + str(resultMax) + ", Min is " + str(resultMin) + " , diff is " + str(resultDiff) + ".")
print("Variation to size ratio is " + str(resultVarToSizeRatio))
