from time import sleep
from espNeoPixelClass import setNeo, red, green, blue, white, off, purple

setNeo(white, 4)


from testPWM import setPWM as vib


for _ in range(4, 11):
    vib(_)
    setNeo(green)
    sleep(.5)
    vib(0)
    setNeo(purple)
    sleep(.3)


import reciever.py

