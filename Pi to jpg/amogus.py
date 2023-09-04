from PIL import Image

# Get pi
with open('amogus.bin', 'rb') as pifile:
    piBytes = pifile.read()
# Convert pi to image
im = Image.frombytes("1", (16, 16), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save('amogus.png', 'PNG')