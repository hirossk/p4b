#スコープが異なれば同じ変数名が利用できます。
def func(x):
    answer = x ** 2 + 2 * x + 3
    x = -1
    #func内で利用可能なxは他の部分で利用されるxとは異なる変数となります。
    return answer

x = 2
#ここでxに代入するとグローバル変数として扱われます。
y = func( x )
print( y )
print( x ) 

x = 4
y = func( x )
print( y )