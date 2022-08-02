#!/usr/bin/python

import sys, getopt
from PIL import Image


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> -s <size>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--size"):
            size = int(arg)
        # Get data
    with open(inputfile, 'rb') as pifile:
        fileBytes = pifile.read()
        # Convert pi to image
    im = Image.frombytes("1", (size, size), fileBytes)
    print(im.format, im.size, im.mode)
    # Save image to file
    im.save(outputfile + '.png', 'PNG')


if __name__ == "__main__":
    main(sys.argv[1:])
