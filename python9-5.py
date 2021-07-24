from PIL import Image,ImageDraw

im = Image.new('RGB', (500, 500),(255,240,230))
#背景をクリーム色で描画用のエリアを作成します。

draw = ImageDraw.Draw(im)
draw.ellipse((100,100,400,400),fill=(230,150,110))
draw.ellipse((190,155,220,210),fill=(0,0,0))
draw.ellipse((280,155,310,210),fill=(0,0,0))
draw.ellipse((200,210,300,290),fill=(230,50,12))
draw.rectangle((250,230,270,250),fill=(255,255,255))

draw.arc((150,140,260,250),-120,-60,fill=(0,0,0),width=5)
draw.arc((240,140,350,250),-120,-60,fill=(0,0,0),width=5)

draw.chord((190,240,310,350),start=-10,end=190,fill=(210,80,82))

im.show()
