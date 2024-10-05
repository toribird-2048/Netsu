import numpy as np
import time
from PIL import Image
import matplotlib.pyplot as plt
import os

height, width = 10,10
blocks = np.zeros((height, width))
delta_blocks = np.zeros((height, width))
spread_rates = np.full((height, width),0.3)
max = 200
min = 0
cycle = 300

fig = plt.figure()
images = []

"""
for k in range(height):
    for l in range(width):
        blocks[k,l] = np.random.randint(0, 100)
"""

blocks[0,0] = 100
for k in range(height-2):
    spread_rates[k,4] = 0
    spread_rates[k,5] = 0

for k in range(cycle):
    print(blocks)
    blocks[0,0] = 100
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
    plt.savefig(f"{k}.png")
    cb.remove()
    plt.cla()
    #time.sleep(1)

for k in range(cycle):
    im = Image.open(f"{k}.png")
    images.append(im)
    os.remove(f"{k}.png")

images[0].save('images.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)