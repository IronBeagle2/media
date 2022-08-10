from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create()

mc.postToChat("Auto Bridge activated");
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x,y-1,z, block.DIAMOND_ORE)
    sleep(0.01)
