import glob
from PIL import Image, ImageDraw

#magic numbers I pulled out from bounds.py
w=3751
h=4464
x1=-300
y1=3652450
v=1518

image = Image.new("RGB",(w,h))
draw = ImageDraw.Draw(image)

l = glob.glob("LO19_050M_3318*.ort")

for item in l:
    f=open(item)
    for line in f:
        s=line.split()
        if len(s)>=3:
            x=int(float(s[0]))-x1
            y=int(float(s[1]))-y1
            c=float(s[2])*10
            r=int(c)/256
            g=int(c)%256
            #print x/25,y/25,c
            draw.point((x/25,y/25),fill=(r,g,0))
    print item

del draw
image.save("output-16bit.png","PNG")
