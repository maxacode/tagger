from time import sleep
#from npDone import setNeo, red, green, blue, white, off
#s#etNeo(green)

# sleep(2)
# setNeo(blue)
# sleep(2)
#import blinker

from blinker import lon, loff, tester

ledON = lon
ledOFF = loff
#tester()
ledON()
sleep(1)
ledOFF()
sleep(3)
ledON()

import base
# 

