from PIL import Image,ImageDraw #ImageDrawのインポートを追加する

im = Image.new('RGB', (500, 300))
draw = ImageDraw.Draw(im) #描画用のオブジェクトを生成する

draw.line((50,50,150,50)) #x,y座標を指定して線を引く 
draw.line((50,100,150,150))

im.show()