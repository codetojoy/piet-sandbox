
import os, sys
import numpy as np

from PIL import Image

# colours
C0 = 0xC0
black = [0, 0, 0]
white = [255, 255, 255]

light_cyan = [C0, 255, 255]
cyan = [0, 255, 255]
dark_cyan = [0, C0, C0]

green = [0, 255, 0]

blue = [0, 0, 255]
dark_blue = [0, 0, C0]

h, w = 270, 270
data = np.zeros((h, w, 3), dtype=np.uint8)

# [a:b, c:d]
# a,b is range of h
# c,d is range of w
# data[0:20, 0:80] = blue is a wide rectangle
#   - (0,0) to (20,80) where (h,w)

def b(n, block):
    """N blocks"""
    return (n * block)

block = 9
b1 = b(1, block)
b2 = b(2, block)
b3 = b(3, block)
b4 = b(4, block)

offset = 5
s2 = b2 - offset
s3 = b3 + offset

data[0:h, 0:w] = black
data[0:b1, 0:b1] = blue
data[0:b1, b1:b2] = dark_blue
data[0:b1, b2:b3] = cyan
data[b1:b3, b2:b4] = dark_cyan
# stopper
data[b2:b3, b1:b2] = cyan
# top stopper
# data[s2:b2, b1:s2] = cyan
# bottom branch
data[b3:s3, b1:s2] = cyan
# bottom stopper
data[s3:s3+offset, b1-(1 *offset):s2+(2*offset)] = cyan

# write image

img = Image.fromarray(data, 'RGB')
img.save('print_q.png')
# img.show()

print("Ready.")
