from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# pos = mc.player.getPos()
x, y, z = mc.player.getPos()
while True:
    mc.setBlocks(x,y-1,z,x+10,y-1,z-30,20)

# 89 glowstone
# 98 stone bricks 
# print(type(pos))
# mc.setBlocks(pos.x-146,-200,pos.z-146,pos.x-146,0,146,46.1)
"""for i in range(106):
    mc.setBlock(pos.x+i,pos.y-1,pos.z,2)
    mc.setBlock(pos.x+i,pos.y,pos.z,i)
    mc.postToChat(i)
mc.postToChat("XD")
while False:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-2,pos.y-1,pos.z-2,pos.x+2,pos.y-1,pos.z+2,0)

mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x+128,pos.y-1,pos.z+128,4)
mc.setBlocks(pos.x,pos.y,pos.z,pos.x+128,pos.y+200,pos.z+128,0)

mc.setBlocks(pos.x-5,pos.y-1,pos.z-5,pos.x+5,pos.y+10,pos.z+5,3)

mc.setBlocks(pos.x-4,pos.y,pos.z-4,pos.x+4,pos.y+9,pos.z+4,0)

mc.setBlock(pos.x,pos.y,pos.z,1)

mc.setBlocks(pos.x,pos.y,pos.z,pos.x,pos.y-100,pos.z,46,1)
# tnt 46

while False:
   mc.postToChat(input("-"))

# mc.setBlocks(-100,-100,-100,100,100,100,0)

while False:
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-10,pos.y-1,pos.z-10,pos.x+10,pos.y-1,pos.z+10,0)
"""

# mc.setBlocks(pos.x,pos.y-1,pos.z,pos.x-11,pos.y-2,pos.z-11,10)
# mc.setBlocks(pos.x,pos.y,pos.z,pos.x-11,pos.y+10,pos.z-11,0)