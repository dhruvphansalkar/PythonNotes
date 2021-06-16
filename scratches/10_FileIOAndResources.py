# Resources - Program elements that must be released or closed after use

#open() - opens a file for reading and writing
# params - 1. file - Path to file| 2. mode - read, write, append, plus binary or text | 3. encoding - default is utf-8
import sys

print(sys.getdefaultencoding()) # encoding can be different on different systems

#
f = open(file='hello.txt', mode='wt', encoding='utf-8')
# for mode - w -> write, r - > read, a -> append || t -> text, b -> binary

#help(f) help can be called on instances as well.

# writing
print(f.write('what are the roots that clutch, ')) # number of code points written is returned
print(f.write('what branches grow\n')) # responsibility of coder to provide new line
print(f.write('Out of this stony rubbish'))
f.close()

# write() returns the number of code points written, which can be different for different os. dont sum them to get the length of the file



# Reading
g = open('hello.txt', mode = 'rt', encoding='utf-8')
print(g.read(32)) #in text mode reads the number iof characters to read from the file not the bytes
print(g.read()) # will read from character 33 as calling read() moved the pointer forward
print(g.read()) # will be empty as file as already be read

print(g.seek(0)) #will move the pointer to the offset mentioned from the start of the file and return the new file pointer position
# seek in text mode cant move to arbitrary offset, only 0 and values returned from tell() method are valid

# readline
print(g.readline()) #will read till the end of the current line and move to the next line
print(g.readline())
print(g.readline()) # will be empty, file end has been reached

print(g.seek(0))
print(g.readlines()) # returns a list of all the lines
g.close()




#Append
h = open('hello.txt', mode='at', encoding='utf-8')
h.writelines( # pass a list of strings
    [
        'Son of man, \n', #pass the line change char yourself
        'You cannot say, or guess, ',
        'For you know only, \n',
        'A heap of broken images, ',
        'where the sun beats\n'
    ]
)
h.close()

g = open('hello.txt', mode='rt', encoding='utf-8')
print(g.read())
g.close()



#File iteration
f = open('hello.txt', mode = 'rt', encoding= 'utf-8')
for line in f: # files support iterable protocol and hence can be iterated on
    print(line) # double spacing bw lines occurs since each line in ended with /n and print adds its own
f.close()

f = open('hello.txt', mode = 'rt', encoding= 'utf-8')
for line in f: # files support iterable protocol and hence can be iterated on
    sys.stdout.write(line) #No double spacing since we are using write(same as write()) instead of print()
f.close()



#Finally
from itertools import count, islice
'''Generate Recaman's sequence'''
def sequence() :
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c

def write_sequence(filename, num):
    """Write the sequence"""
    f1 = open(filename, mode='at', encoding='utf-8')
    f1.writelines(f'{r}\n' for r in islice(sequence(), num + 1))
    f.close()

    #with block implementation
    #with open(filename, mode='at', encoding='utf-8') as f1:
        #f1.writelines(f'{r}\n' for r in islice(sequence(), num + 1))

write_sequence('recaman_sequence.txt', 10)


def read_sequence(filename): #add a invalid string to the file to trigger a exceptional case
    """Read the sequence"""
    g1 = open(filename, mode='rt', encoding='utf-8')
    series = []

    try:
        # return [int(line.strip()) for line in g1] -> list comprehension alternative to for loop
        for line in g1:
            a = int(line.strip()) # error will execute on this line if the read value is not an integer
            series.append(a)
    finally: # will execute after exception
        print('g1 closed')
        g1.close() # if error occurs, close() will not be executed unless it is inside finally
    return series

print(read_sequence('recaman_sequence.txt'))




# With block - Control flow structure which pairs open with close automatically, used with objects supporting context manager protocol

def read_series_with_block(filename):
    with open(filename, mode='rt', encoding='utf-8') as g2:
        return [int(line1.strip()) for line1 in g2] # close will be called when execution exits the block



#Binary Files

def write_grayscale(filename, pixels):
    """Creates and writes grayscale BMP file
    :arg
        filename: the name of the BMP file
        pixel: A rectangular image stored as a sequence of rows
        Each row must be an iterable series of integers in the range 0-255.

    :raises
    value error: if any integer values are out of range
    OSError If the file could not be written"""

    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM') #all bmp files start with a byte sequence BM

        size_bookmark = bmp.tell() # the next 4 bits hold the file size as 32 bit
        bmp.write(b'\x00\x00\x00\x00') # little endian integer. Zero placeholder for now

        bmp.write(b'\x00\x00')  # Unused 16 bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16 bit integer - should be zero

        pixed_offset_bookmark = bmp.tell() #the next 4 bytes hold the integer offset to the pixel data
        bmp.write(b'\x00\x00\x00\x00') # Zero placeholder for now

        #Image header
        bmp.write(b'\x28\x00\x00\x00') #image header size in bytes
        bmp.write(width.to_bytes())    #image width in pixels
        bmp.write(height.to_bytes()) #image height in pixels
        bmp.write(b'\x01\x00')             #number of image planed
        bmp.write(b'\x08\x00')             #Bits per pixel 8 for greyscale
        bmp.write(b'\x00\x00\x00\x00')     #No compression
        bmp.write(b'\x00\x00\x00\x00')     #Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')     #Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')     #Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')     #Use whole color table
        bmp.write(b'\x00\x00\x00\x00')     #All colors are important

        #Color palette
        for c in range(256):
            bmp.write(bytes((c,c,c,0))) # blue, green, red, zero

        #pixel data
        pixel_data_bokmark = bmp.tell()
        for row in reversed(pixels): #bmp files are bottom to top
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4-(len(row) % 4)) % 4) #pad row to multiple of row_bytes
            bmp.write(padding)

        # end of file
        eof_bookmark = bmp.tell()

        # fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(eof_bookmark.to_bytes())

        # fill in pixel offset placeholder
        bmp.seek(pixed_offset_bookmark.to_bytes())

# Bitwise operators - & : bitwise and, >> : Right-Shift


# File like object - objects that behave like files

def word_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]

with open('hello.txt', mode='rt', encoding='utf-8') as real_file:
    print('len per line from file')
    print(word_per_line(real_file))

from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as web_file:
    print('len per line from http resource')
    print(word_per_line(web_file))

# this demonstrates use of file like object using duck typing





