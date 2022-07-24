# リストに記載されているデータの平均値を求めるプログラムを作ります
# 同じ処理を２回繰り返すことを考えます

# 関数はdef文で定義を行います。
# 関数はブロックになり「:」で開始しインデント（字下げ）します
def listave(listdata):
    total = 0
    # リストのデータを取り出しvalに入れながら繰り返す
    for val in listdata:
        total = total + val
    # len(listdata)はlistdataのサイズ（大きさ）を取得できます
    ave = total / len(listdata)
    # 関数として戻り値がある場合はreturn文で値を指定します
    return ave

# 簡単なデータを用意します１
listdata1 = [2,4,3,5,1]
# 関数listaveを呼び出し結果を変数answer に代入します
answer = listave(listdata1)
# 結果を表示します

# 簡単なデータを用意します２
listdata2 = [6,9,7,10,8,1,3,5,2,4]
# 関数を呼び出し結果を変数answer に代入します

# 結果を表示します