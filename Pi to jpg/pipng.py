from PIL import Image

# Get pi
with open('pi.bin', 'rb') as pifile:
    piBytes = pifile.read()
# Convert pi to image
size = 181
im = Image.frombytes("1", (size, size), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save('pibin.png', 'PNG')
