
import os, sys
import numpy as np

from PIL import Image

# colours
black = [0, 0, 0]
white = [255, 255, 255]

light_cyan = [192, 255, 255]
cyan = [0, 255, 255]

green = [0, 255, 0]

blue = [0, 0, 255]
dark_blue = [0, 0, 192]

h, w = 270, 270
data = np.zeros((h, w, 3), dtype=np.uint8)

# [a:b, c:d]
# a,b is range of h
# c,d is range of w
# data[0:20, 0:80] = blue is a wide rectangle
#   - (0,0) to (20,80) where (h,w)
data[0:511, 0:511] = black
data[0:80, 0:80] = blue
data[0:80, 80:160] = dark_blue
data[0:160, 160:270] = cyan
data[120:220, 160:270] = white
data[190:220, 40:160] = green
data[140:190, 40:130] = green
data[220:240, 40:130] = green

# write image

img = Image.fromarray(data, 'RGB')
img.save('print_q.png')
img.show()

print("Ready.")
