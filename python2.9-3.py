#引数にはなにも指定しません。
def func():
    answer = x ** 2 + 2 * x + 3
    #ここで利用されている変数xは7行目で代入されている変数xそのものです。
    return answer

x = 2
#ここでxに代入するとグローバル変数として扱われます。
y = func()
print( y )

x = 4
y = func()
print( y )