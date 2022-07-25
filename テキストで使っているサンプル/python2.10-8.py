from PIL import Image

img = Image.open("imagesample/sample01.jpg")  
# 画像の読み込み

img = img.rotate(30)
#回転画像をもとの変数（オブジェクト）に入れています

img.show()  # 画像表示
