# 並べ替えをするプログラム

arr_var = [5,3,2,4,1]
# バブルソートは２重ループになります
# 外ループ
for i1 in range(4):
    # 内ループ
    for i2 in range(4-i1):
        if arr_var[i2] > arr_var[i2 + 1]:
            #入れ替え処理
            temp = arr_var[i2]
            arr_var[i2] = arr_var[i2 + 1]
            arr_var[i2 + 1] = temp

# 並べ替え後の処理
print(arr_var)

# # もう一度行いたい場合
# # 関数化することで何度も呼び出せることとプログラム本体をコンパクトにできる
# def arr_sort(arr_var):
#     # 配列のサイズが変更しても大丈夫なようにループ回数を
#     # 取得する
#     arr_size = len(arr_var) - 1
#     # 外ループ
#     for i1 in range(arr_size):
#         # 内ループ
#         for i2 in range(arr_size-i1):
#             if arr_var[i2] > arr_var[i2 + 1]:
#                 #入れ替え処理
#                 temp = arr_var[i2]
#                 arr_var[i2] = arr_var[i2 + 1]
#                 arr_var[i2 + 1] = temp

# arr_var = [1,4,7,2,6,3,9,8,5]
# arr_sort(arr_var)
# print(arr_var)
# arr_var = [5,6,10,20,19,16,15,1,3,12,8,25,24,2,30,9]
# arr_sort(arr_var)
# print(arr_var)