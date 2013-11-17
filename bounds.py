import fileinput
import glob

x1=23525
x2=0
y1=3705525
y2=0
h=0

l = glob.glob("*.ort")

for line in fileinput.input(l):
    s=line.split()
    #print s
    #break
    if len(s)>=3:
        x1=min(x1, float(s[0]))
        x2=max(x2, float(s[0]))
        y1=min(y1, float(s[1]))
        y2=max(y2, float(s[1]))
        h=max(h, float(s[2]))

print x1, x2, y1, y2, h, (x2-x1)/25, (y2-y1)/25
