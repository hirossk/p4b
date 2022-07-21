# 本格的なリストの理解

# リストにはリストそのものを操作する機能があります
# リストの定義で要素を空にして生成することもできます
listdata = []

# リストの最後にデータを追加します
#listdata.append(1)
#listdata.append(2)
#listdata.append(3)
#listdata.append(4)
#listdata.append(1)
#listdata.append(2)
#listdata.append(3)
#listdata.append(4)

# リストを出力します
#print(listdata)

# さらにリストを追加します
#listdata.append(5)

# リストを出力します
#print(listdata)

# リストの長さを出力します（len関数の復習）
#print(len(listdata))

# リストの要素を削除します。この例ではリストの2番目の要素を取り出します
# 先頭のデータは0番目なのを忘れないようにしましょう
#listdata.pop(2)
#print(listdata)

# リストの中で一致するものを数えることができます
#print(listdata.count(2))

# リストの中で指定の値と一致する最初のデータを削除します
#listdata.remove(4)
#print(listdata)

# リストの中で指定の値と一致する最初の場所（インデックス）を
# 変数iに取得します
#i = listdata.index(3)
#print(i)

# リストに値が含まれているかどうかチェック（真理値）します
#print(9 in listdata)
#print(3 in listdata)

# リストの値の並べ替えもできます
#listdata.sort()
#print(listdata)
## 逆順にします
#listdata.sort(reverse=True)
#print(listdata)