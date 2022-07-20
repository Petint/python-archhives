from PIL import Image

with open('pi.txt', 'rt') as pifile:
    pi = int(pifile.read())

piBytes = pi.to_bytes(2, 'big')
im = Image.open(piBytes)
print(im.format, im.size, im.mode)
