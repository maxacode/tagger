# from espNeoPixelClass import NeoPixelController as npc, r,g,b,w
# 
# np = npc()
# 
# np.setNeo("green")
# 
# 
# setNeo = np.setNeo
# 
# setNeo(b)

from espNeoPixelClass import setNeo, red, green, blue, white, off, purple


setNeo('green', 10)
print(setNeo('white',8,reset = False))

setNeo(off, 10)