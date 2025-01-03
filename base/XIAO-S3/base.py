"""
Base v1.6

 - setup espNow stuff
 - main - all tasks with asncio
 - time since last button press tracked.
1.5
LED green before deepsleep so it stays on to get attensin
npDOne - greren value cahgned to high.

# TODO Migrate to espNeoPixelClass

deepsleep off
setNeo replased with ledON/OFF
npDone.py
"""
import time, asyncio
from machine import Pin, deepsleep, lightsleep, DEEPSLEEP, SLEEP,reset_cause, TouchPad
from time import sleep
import network, espnow
from json import dumps
import esp32

#from npDone import setNeo, red, green, blue, white, off
from blinker import lon, loff, tester
ledON = lon
ledOFF = loff
ledON()



dsEnabled = True

def writeFile(*args, **kwargs )-> None:
    """
    Write data to a file with time and pipe separator
    """
    try:
        ledON()
        curTime = time.time()
        #print(curTime, args, kwargs)
        #                90     84 = 6sec
        time_elapsed = curTime-tLast
        sec = time_elapsed % 60
        min = (time_elapsed // 60) % 60
        HR = time_elapsed // 3600

        timeSinceLast = (f"{HR=} {min=}, {sec=}")
            
        data = f'{curTime=} | {timeSinceLast=} || {args} {kwargs} \n'
        print(data)
    except Exception as Error:
        print(Error)
        data = f'Err writeFile {Error=} \n{time.time()}'
        print(data)
    finally:
        with open('logBase.txt', 'a+') as file:
            file.write(data)
            
    #await asyncio.
   # sleep(.3)
    
def espTX()-> None:
    """
    Send commands to peer broadcast 
    """
    global kA, e
    kA = 0 #reset keepAlive counter to 0
    writeFile('start espTX')
    ledON()
    data = dumps({"tagger":"wakeup"})
    e.send(peer1, str(data), True)     # send commands to pear 1
   # await asyncio.
    #sleep(.3)

    writeFile('end espTX')
    ledON()
    
def keepAlive()-> None:

    """    
    Sleep and increase counter by X and if button is pressed reset it. 
    After Y time, do deep sleep
    
   1 machine.PWRON_RESET
   2 machine.HARD_RESET
   3 machine.WDT_RESET
   4 machine.DEEPSLEEP_RESET
   5 machine.SOFT_RESET
   
    """
    kA = 0
    while True:
        ledOFF()
        sleep(.5)
        if kA >= 10:
            writeFile(f'Going to ds: {kA=}')
            #setNeo((20,20,20))
            #sleep(1)
            if dsEnabled:
                #writeFile('ln 62')
                ledOFF()
                #sleep(1)
                writeFile(f'GOING DEEPSLEE')
                #kA = 0             
                deepsleep() # deepsleep()

            else:
                writeFile('dS False, sleep , ka=0')
                sleep(1)
                kA = 0
        else:
            kA += 1
            #setNeo((20,0,30))
            #await asyncio.
            # Try light sleep or deepsleep
            writeFile(f'awaiting sleep: {kA=}')
            espTX()
            ledON()
            sleep(.5)

            
async def main()-> None:
    """
    Main Loop to handle everything
    Params: None
    Returns: None
    """
   # writeFile('IRQ Setup')
    #butt1 = Pin(44, Pin.IN, Pin.PULL_UP)  # pin 43
    #butt1.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=espTX)
    asyncio.run(keepAlive())

try:
    with open('logBase.txt', 'r') as file:
        tLast = int(file.readlines()[-1])
except:
    tLast = 0 

writeFile(' ---------------------------- ')
writeFile(f"\n\n NEW INTSTANCE | {tLast=}\n")
writeFile(f"ln 104 reset_cause: {reset_cause()=}", type(reset_cause()))


    

### Setup ESP Now
sta = network.WLAN(network.STA_IF)    # Enable station mode for ESP
wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(False)
wlan_sta.active(True)
sta.disconnect()        # Disconnect from last connected WiFi SSID
e = espnow.ESPNow()     # Enable ESP-NOW
e.active(True)
peer1 = b'\xff\xff\xff\xff\xff\xff' #broadcast
#peer1 = b"H'\xe2\r\x80h"
try:
    e.add_peer(peer1)
except:
    pass

butt1 = Pin(8, Pin.IN)#, Pin.PULL_DOWN)  # pin 43
#butt1.off()
#esp32.wake_on_ulp(False)
#esp32.gpio_deep_sleep_hold(False)
#     touchVal = touchPin.read()

# 
# touchPin = Pin(2, Pin.IN)
# touch = TouchPad(touchPin)
# 
# touch.config(40000)
# 
# from time import sleep
# 
# for _ in range(0,3):
#     touchVal = touch.read()
#     writeFile(touchVal)
#     sleep(.4)
    

#esp32.wake_on_touch(True)
esp32.wake_on_ext0(pin = butt1, level = esp32.WAKEUP_ANY_HIGH)
#esp32.wake_on_ext0(pin = butt1, level = esp32.WAKEUP_ALL_LOW)

keepAlive()
 




