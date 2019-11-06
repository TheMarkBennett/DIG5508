#%% Old School Filter

from PIL import Image, ImageDraw
import random

filename = "project2\Mark-Bennett.png"

def roateImg(filename):

    img = Image.open(filename).convert('1')

    width, height = img.size

    imgoverlay =  Image.new('RGBA', (width, height), "green")

    mask = Image.new("L", img.size, 150)

    im = Image.composite(img, imgoverlay, mask)

    for i in range(10,50):

        h = random.randint(0, height) 

        for x in range(0,height):

            im.putpixel((x, h), (0,100,0,255))

    return im


roateImg(filename)

# %%
