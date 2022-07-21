# 繰り返し表現の変更
# 繰り返し加算をすることを考えましょう
sum = 1 + 2 + 3 + 4 + 5

# 同じ表現への変更　6行目から11行目
#sum = 0
#sum = sum + 1
#sum = sum + 2
#sum = sum + 3
#sum = sum + 4
#sum = sum + 5

# 増やす値（incv）を変化させる　14行目から25行目
#sum = 0
#incv = 0
#incv = incv + 1
#sum = sum + incv
#incv = incv + 1
#sum = sum + incv
#incv = incv + 1
#sum = sum + incv
#incv = incv + 1
#sum = sum + incv
#incv = incv + 1
#sum = sum + incv

# 5回繰り返すプログラム例 28行目から33行目
#sum = 0
#incv = 0
# for文で5回繰り返す
#for times in range(5):
#    incv = incv + 1
#    sum = sum + incv

# 1,3,5,7,9と奇数値のみ加算するプログラムに変更 36行目から40行目
#sum = 0
#incv = 0
#for times in range(5):
#    incv = incv + 1
#    sum = sum + incv

# 36行目から40行目のプログラムを変数incvを使わないように変更
# してみてください。rangeの引数を変更し、for文の変数を活用
# しましょう

print("合計 = ",sum)