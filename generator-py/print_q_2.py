
import os, sys
import numpy as np

from PIL import Image

# colours
black = [0, 0, 0]
white = [0xFF, 0xFF, 0xFF]

light_yellow = [0xFF, 0xFF, 0xC0]
yellow = [0xFF, 0xFF, 0]

light_cyan = [0xC0, 0xFF, 0xFF]
cyan = [0, 0xFF, 0xFF]
dark_cyan = [0, 0xC0, 0xC0]

green = [0, 0xFF, 0]

light_blue = [0xC0, 0xC0, 0xFF]
blue = [0, 0, 0xFF]
dark_blue = [0, 0, 0xC0]

light_magenta = [0xFF, 0xC0, 0xFF]
magenta = [0xFF, 0, 0xFF]
dark_magenta = [0xC0, 0, 0xC0]

# codel is 3x3
block = 3
# image is 60x60
image_factor = 20
h, w = image_factor * block, image_factor * block
image_factor2 = 8
h2, w2 = image_factor2 * block, image_factor2 * block
data = np.zeros((h, w, 3), dtype=np.uint8)

# [a:b, c:d]
# a,b is range of h
# c,d is range of w
# data[0:20, 0:80] = blue is a wide rectangle
#   - (0,0) to (20,80) where (h,w)

def b(n, block):
    """N blocks"""
    return (n * block)

b1 = b(1, block)
b2 = b(2, block)
b3 = b(3, block)
b4 = b(4, block)
b4a = b4 + 1
b5 = b(5, block)
b6 = b(6, block)
b7 = b(7, block)

offset = 5
s4 = b4 - offset
# s3 = b3 + offset

data[0:h, 0:w] = white
data[0:h2, 0:w2] = black
data[0:b1, 0:b1] = blue            # push 9
data[0:b1, b1:b2] = dark_blue      # push 9
data[0:b1, b2:b3] = light_blue     # multiply
data[0:b1, b3:b4] = dark_magenta   # out(c)
data[0:b1, b4:b4a] = blue          # push 3
data[b1:b2, b4:b4a] = dark_blue    # pointer
data[b2:b3, b4:b4a] = light_yellow # push
# stopper
data[b2:b3, b4a:b5] = yellow
data[b3:b4, b4a:b5] = yellow
# bottom stopper
data[b4:b5, s4:b7] = yellow

# write image

img = Image.fromarray(data, 'RGB')
img.save('print_q_2.png')
img.show()

print("Ready.")
