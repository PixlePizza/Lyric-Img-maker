from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from pprint import pprint



def new_IMAGE(msg, count):
    W, H = (500,500)

    count = str(count)

    img = Image.new("RGBA",(W,H),(55, 135, 159))
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(msg)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="black")

    img.save("Shine i wanna/"+count+" I just wanna shine.png", "PNG")

    return

lyrixfile = open("lyrix.txt","r")
lyrix = lyrixfile.read()
lyrix = lyrix.splitlines()

for i in range(0, len(lyrix)):
    new_IMAGE(lyrix[i], i)
