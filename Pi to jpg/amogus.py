from PIL import Image

name = "buddha"
# size = 1000
# Get pi
with open(name+'.bin', 'rb') as pifile:
    piBytes = pifile.read()
# Convert pi to image
im = Image.frombytes("1", (1920, 1080), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save(name+'.png', 'PNG')