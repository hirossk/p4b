# リストの平均値を求める関数を定義しています
def listave(listdata):
    total = 0
    # リストのデータを取り出しvalに入れながら繰り返す
    for val in listdata:
        total = total + val
    # len(listdata)はlistdataのサイズ（大きさ）を取得できます
    ave = total / len(listdata)
    return ave
