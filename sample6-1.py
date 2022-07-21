# 乱数を生成して本当に均等になるか確認してみましょう

import random

# randrange関数を使って0～2の乱数を生成してリストに格納します
# 空のリストを生成します
#randlist = []

# for文でリストにランダムデータを追加します
#for cnt in range(10):
#   randlist.append(random.randrange(3))
# 生成したリストを出力します
#print(randlist)

# データが少ないと0～2のデータには偏りが大きいはずなので
# 確認してみましょう。概ね33%になるのはどのあたりでしょうか
#print('0の数 = ', randlist.count(0))
#print('1の数 = ', randlist.count(1))
#print('2の数 = ', randlist.count(2))
