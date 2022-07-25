#Pillowライブラリを利用する場合は名称PILを使う宣言が必要で、
#import文で描画に必要なライブラリを指定する。
#このプログラムはPillow形式からOpenCV形式に変換して表示するプログラム
from PIL import Image
import cv2
import numpy as np

im = Image.new('RGB', (500, 300)) #イメージを作成する。'RGB'は赤・緑・青の色指定を意味する
im = Image.new('RGB', (500, 300),( 255, 0, 0)) #イメージを作成する。'RGB'は赤・緑・青の色指定を意味する

out_image = np.asarray(im)  # 入力画像をndarray型に変換する

if out_image.shape[2] == 3:
    out_image = cv2.cvtColor(out_image, cv2.COLOR_RGB2BGR)
#im.show() #イメージを表示する
cv2.imshow("title",out_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
