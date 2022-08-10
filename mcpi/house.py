from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
x, y, z = mc.player.getPos()

mc.postToChat("House v0 by Dejvoss.cz");

#Side walls
mc.setBlocks(x+5,y,z, x+10, y+2, z, block.COBBLESTONE.id)
mc.setBlocks(x+5,y,z+5, x+10, y+2, z+5, block.COBBLESTONE.id)

#Back and Front walls
mc.setBlocks(x+5,y,z, x+5,y+2,z+5, block.COBBLESTONE.id)
mc.setBlocks(x+10,y,z, x+10,y+2,z+5, block.COBBLESTONE.id)

#Floor
mc.setBlocks(x+5,y-1,z, x+10,y-1,z+5, block.BRICK_BLOCK.id)

#Roof
mc.setBlocks(x+5,y+3,z, x+10,y+3,z+5, block.WOOD_PLANKS.id)

#Carve doors
mc.setBlocks(x+5,y,z+2, x+5, y+1, z+3, block.AIR.id)
