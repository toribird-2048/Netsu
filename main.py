import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation

height, width = 10,10
blocks = np.zeros((height, width))
delta_blocks = np.zeros((height, width))
spread_rate = 0.1
max = 100
min = 0

fig = plt.figure()
images = []

"""
for k in range(height):
    for l in range(width):
        blocks[k,l] = np.random.randint(0, 100)
"""

blocks[0,0] = 100

for k in range(1000):
    print(blocks)
    for i in range(height):
        for j in range(width):
            if i == 0:
                delta_blocks[i,j] += 0
            else :
                delta_blocks[i,j] += (blocks[i-1,j] - blocks[i,j]) * spread_rate
            
            if j == 0:
                delta_blocks[i,j] += 0
            else :
                delta_blocks[i,j] += (blocks[i,j-1] - blocks[i,j]) * spread_rate
            
            if i == height-1:
                delta_blocks[i,j] += 0
            else :
                delta_blocks[i,j] += (blocks[i+1,j] - blocks[i,j]) * spread_rate
            
            if j == width-1:
                delta_blocks[i,j] += 0
            else :
                delta_blocks[i,j] += (blocks[i,j+1] - blocks[i,j]) * spread_rate
            
    blocks += delta_blocks
    delta_blocks = np.zeros((height, width))
    images.append(plt.imshow(blocks,cmap=plt.cm.jet,vmax=max,vmin=-min))
    cb = plt.colorbar()
    cb.set_ticks(np.linspace(min, max, 5)) 
    plt.savefig(f"images//{k}.png")
    cb.remove()
    plt.cla()
    #time.sleep(1)
