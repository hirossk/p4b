# 関数と反復、選択の組み合わせの練習
# リストから最大値を求めることを考えましょう

# 関数listmaxを定義します
def listmax(listdata):
    # リストの要素がある間繰り返し最大値を見つけるために
    # 0を仮の最大値としておきます
    max_value = 0
    # listdataの要素がある間valueに取り出しながら繰り返します
    for value in listdata:
        # 「仮の最大値」よりもvalueが大きいかどうか考えます
        # 最近の生徒さんはこのあたりが苦手かもしれません
        if max_value < value:
            # 仮の最大値をvalueにします
            max_value = value
    
    # 繰り返し終了後見つかった最大値を戻り値とします
    return max_value

# 簡単なデータを用意します１
listdata1 = [2,4,3,5,1]
# 関数listmaxを呼び出し結果を変数answer に代入します
answer = listmax(listdata1)
# 結果を表示します
print(answer)

# 簡単なデータを用意します２
listdata2 = [6,9,7,10,8,1,3,5,2,4]
# 関数を呼び出し結果を変数answer に代入します
answer = listmax(listdata2)
# 結果を表示します
print(answer)

