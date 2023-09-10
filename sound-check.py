import winsound
import time

def make_sound(type: bool, iterations, length):
    if type: frequency = 2000
    else: frequency = 500
    for i in range(iterations):
        winsound.Beep(frequency, length)
        time.sleep(0.1/1000)

for i in range (20):
    make_sound(True, i, 50)
    time.sleep(1)