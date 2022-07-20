from PIL import Image

# Get pi
with open('pi.txt', 'rt') as pifile:
    piBytes = bytes(pifile.read(), pifile.encoding)
# Convert pi to image
im = Image.frombytes("RGB", (100, 100), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save('piimg.jpg', 'JPEG')
