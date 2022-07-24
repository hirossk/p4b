val = [2,5,8,3,1]
#選択ソート法
for index1 in range(4):
    #比較範囲の先頭の要素を最小値とみなし一時保管する。
    tempval = val[index1]
    tempmin = tempval
    repindex = index1
    for index2 in range(index1 + 1, 5):
        #比較範囲の次の値から最後まで繰り返す。
        if tempmin > val[index2] :
            #比較範囲の中から最小値とみなした値よりも小さい値を見つけたら一時保管する
            tempmin = val[index2]
            repindex = index2
    #先頭の値と最小値の入れ替え(本当は違ったときだけ入れ替え)
    #if 違ったときだけの条件 :
    tempval = val[index1]
    val[index1] = val[repindex]
    val[repindex] = tempval
print(val)
