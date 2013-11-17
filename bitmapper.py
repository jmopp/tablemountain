#Produces a string of 16-bit integers from our bitmap

from PIL import Image

image = Image.open("heightmap.bmp")

x=704
y=520

bits = open("web/bits.bin","w")

for j in range(520):
    for i in range(704):
        t=image.getpixel((i,j))
        bits.write(chr(t[1])+chr(t[0]))

bits.close()
