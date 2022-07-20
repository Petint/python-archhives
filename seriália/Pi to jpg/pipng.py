from PIL import Image

# Get pi
with open('pi.txt', 'rt') as pifile:
    piBytes = bytes(pifile.read(), pifile.encoding)
# Convert pi to image
size = 892
im = Image.frombytes("1", (size, size), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save('piimg.png', 'PNG')
