from PIL import Image,ImageDraw

im = Image.new('RGB', (500, 300),(255,255,255))
draw = ImageDraw.Draw(im)
draw.line((50,50,150,50),fill=(255,0,0)) #引数に色指定を追加する
draw.line((50,100,150,150),fill=(255,0,0), width = 4)
  #引数に線の幅を指定する
draw.ellipse((150,150,300,300),fill=(0,255,0))
im.show()