import pandas as pd
import os
from PIL import Image, ImageDraw

data = pd.read_csv(os.path.join(os.getcwd(), "data/MNIST/train.csv"))

digit_0 = data.loc[data['label'] == 0]

avr = {}
row = 0
for i, v in enumerate(digit_0.sum()):
    if v > len(digit_0):
        if i in avr:
            avr[i] += v
        else:
            avr[i] = v
a = {}
for i in [{k: v/len(digit_0)} for k,v in avr.items()]:
    a.update(i)

m = max(a.values())

a_p = {}
for i in [{k: (v/m)*100} for k,v in a.items()]:
    a_p.update(i)
#print(a_p)

img = Image.new("L", (28, 28), "black")
pixels = img.load()

for col in range(img.size[0]):
    for row in range(img.size[1]):
        if col*row in a_p.keys():
            print(a_p[col*row])
            pixels[col, row] = int(a_p[col*row])
img.show()
