from PIL import Image,ImageDraw,ImageFilter

img1 = Image.open("imagesample/sample01.jpg") 
img2 = Image.open("imagesample/sample02.jpg") 
img2 = Image.open("imagesample/sample02.jpg").resize((180,150))
# 画像の読み込み


img1.show()  
img2.show()

img3 = Image.new("RGB", img1.size)
img3.paste(img2)

mask = Image.new("L", img1.size, 128)
im = Image.composite(img1, img3, mask)
im = Image.blend(img1, img3, 0.5)
im.show()

mask = Image.new("L", img1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 179, 149), fill=255)
im = Image.composite(img3, img1, mask)
im.show()

mask = Image.new("L", img1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 179, 149), fill=255)
mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
im = Image.composite(img3, img1, mask_blur)

im.show()
# 画像表示