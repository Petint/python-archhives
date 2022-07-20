from PIL import Image

# Get pi
with open('portal_procedural_jiggle_bone.txt', 'rb') as pifile:
    piBytes = pifile.read()
# Convert pi to image
size = 892
im = Image.frombytes("1", (size, size), piBytes)
print(im.format, im.size, im.mode)
# Save image to file
im.save('portal_procedural_jiggle_bone.png', 'PNG')
