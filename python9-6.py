from PIL import Image,ImageDraw
import time

im = Image.new('RGB', (500, 500),(255,255,255))

draw = ImageDraw.Draw(im)

for x in range(0,255):
    draw.ellipse((100 + x,100,400,400),fill=(x,0,255-x))  

im.show()
