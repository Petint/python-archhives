from PIL import Image
from math import sqrt

with open('pi.txt', 'rt') as pifile:
    piBytes = bytes(pifile.read(), pifile.encoding)

im = Image.frombytes("RGB", (100, 100), piBytes)
print(im.format, im.size, im.mode)
