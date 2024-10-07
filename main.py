import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt
import os
import random
import copy

height, width = 3,3
blocks = np.zeros((height, width))
delta_blocks = np.zeros((height, width))
spread_rates = np.full((height, width),0.3)
spread_rate_max = 0.3
max = 100
min = 0
cycle = 100
point_temp = 100

fig = plt.figure()
images = []

"""
for k in range(height):
    for l in range(width):
        blocks[k,l] = np.random.randint(0, 100)
"""

for k in range(height):
    for l in range(width):
        spread_rates[k,l] = np.random.random() * spread_rate_max

im = plt.imshow(spread_rates,cmap=plt.cm.jet,vmax=1,vmin=0)
cb = plt.colorbar()
cb.set_ticks(np.linspace(0,1,11)) 
plt.savefig(f"spread_rates.png")
cb.remove()
plt.cla()

#"""
def cycle_process(hotpoint_x:int,hotpoint_y:int,output_num:int):
    global height
    global width
    global blocks
    global delta_blocks
    global point_temp

    for k in range(cycle):
        print(blocks)
        print(k)
        blocks[hotpoint_x,hotpoint_y] = point_temp
        for i in range(height):
            for j in range(width):
                if i == 0:
                    delta_blocks[i,j] += 0
                else :
                    delta_blocks[i,j] += (blocks[i-1,j] - blocks[i,j]) * spread_rates[i,j] * spread_rates[i-1,j]
                
                if j == 0:
                    delta_blocks[i,j] += 0
                else :
                    delta_blocks[i,j] += (blocks[i,j-1] - blocks[i,j]) * spread_rates[i,j] * spread_rates[i,j-1]
                
                if i == height-1:
                    delta_blocks[i,j] += 0
                else :
                    delta_blocks[i,j] += (blocks[i+1,j] - blocks[i,j]) * spread_rates[i,j] * spread_rates[i+1,j]
                
                if j == width-1:
                    delta_blocks[i,j] += 0
                else :
                    delta_blocks[i,j] += (blocks[i,j+1] - blocks[i,j]) * spread_rates[i,j] * spread_rates[i,j+1]
                
        blocks += delta_blocks
        delta_blocks = np.zeros((height, width))
        im = plt.imshow(blocks,cmap=plt.cm.jet,vmax=max,vmin=-min)
        cb = plt.colorbar()
        cb.set_ticks(np.linspace(min, max, 5)) 
        plt.savefig(f"imagegifs/images/{k}.png")
        cb.remove()
        plt.cla()
        #time.sleep(1)

    for k in range(cycle):
        images.append(Image.open(f"imagegifs/images/{k}.png"))
        os.remove(f"imagegifs/images/{k}.png")

    images[0].save(f'imagegifs/{output_num}images.gif',
                save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
#"""

cycle_process(0,0,0)