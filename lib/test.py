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

from espNeoPixelClass import setNeo, r,g,b,w

setNeo('green')
print(setNeo(w,15,reset = False))

