import numpy as np
import matplotlib.pyplot as plt
width = 300
height = 200
camera = np.array([0, 0, 1])
ratio = float(width) / height
screen = (-1, 1 / ratio, 1, -1 / ratio) # слева, сверху, справа, снизу
image = np.zeros((height, width, 3))
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        # image[i, j] = ...
        print("progress: %d/%d" % (i + 1, height))
plt.imsave('image.png', 1)