# リストに記載されているデータの平均値を求めるプログラムを作ります
# 同じ処理を２回繰り返すことを考えます

# 簡単なデータを用意します
listdata1 = [2,4,3,5,1]

# 変数totalを0で初期化します
total = 0
# リストのデータを取り出しvalに入れながら繰り返す
for val in listdata1:
    total = total + val
# len(listdata1)はlistdata1のサイズ（大きさ）を取得できます
ave = total / len(listdata1)
print("average1 = ", ave)

listdata2 = [6,9,7,10,8,1,3,5,2,4]
# 変数totalを0で初期化します
total = 0
# リストのデータを取り出しvalに入れながら繰り返す
for val in listdata2:
    total = total + val
# len(listdata2)はlistdata2のサイズ（大きさ）を取得できます
ave = total / len(listdata2)
print("average2 = ", ave)
