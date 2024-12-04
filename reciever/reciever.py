"""
Receiver v2 - Works
 - esp now Recieves and prints
 - VIB works
 - 

2.2 11/28
- added PWM VIB

v2.1 11/27
- made recv blocking instead of 5sec timeout

"""
from machine import Pin
import espnow
import time, asyncio
import network
from json import loads

from npDone import setNeo, red, green, blue, white, off
from testPWM import setPWM as vib

setNeo(white)
time.sleep(1)

#{"tagger":"wakeup"}
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()                # Disconnect from last connected WiFi SSID

e = espnow.ESPNow()                  # Enable ESP-NOW
e.active(True)



    
def writeFile(*args, **kwargs )-> None:
    """
    Write data to a file with time and pipe separator
    """
    setNeo(red)
    curTime = time.time()
    print(curTime, args, kwargs)

    with open('logReciever.txt', 'a+') as file:
        file.write(f'{curTime=} || {args} {kwargs} \n')
    #await asyncio.
   # sleep(.3)
vibCounter = 0 
async def espnow_rx():
    writeFile(f'espnow-rx-start | {vibCounter=}')
    tNow = time.time()
    global vibCounter
    while True:
        setNeo(blue)
        host, msg = e.recv()
        if msg:
            # load data fro JSON
#             print(msg)
#             print(loads(msg)['tagger'])

            try:
                msgJ = loads(msg)
            except Exception as Error:
                msgJ = msg
                writeFile(f'msgJ not JSON : {Error=}')
            finally:
                writeFile(f'finally: {e.peers_table=}  :  {msgJ=}')
            
            if "tagger" in msgJ:
                vibCounter +=1
                if "wakeup" == msgJ['tagger']:
                    setNeo(green) # green/
                    writeFile('tagger:wakeup: vib.on')
                    #await asyncio.sleep(2) #keeps buzzing till last packet is recieved.
                    for x in range(0, 5):
                        vib(vibCounter)
                        time.sleep(.5)
                        vib(0)
                        time.sleep(.2)
                    writeFile('tagger:wakeup: vib.off')
                else:
                    writeFile('not wakeup in msgJ')
            else:
                writeFile("not tagger in msgJ")
                

async def keepAlive():
    while True:
        print('keepAlivesleep')

        await asyncio.sleep(500)
        print('sleep')
        
async def main():
    from time import sleep
    #sleep(4)
    asyncio.create_task(espnow_rx())
    
    asyncio.run(keepAlive()) #type: ignore


tNow = time.time()
writeFile(f"\n\n NEW INTSTANCE | {tNow=}\n")


asyncio.run(main())

