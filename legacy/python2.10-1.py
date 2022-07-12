#モジュールを利用する場合import文で読み込みを行う
import random
import time
import math

for i in range(10):
    #ループの回数を表示する
    print( i )
    #現在時刻を取得し表示する
    print( time.ctime() )
    #カウンターの平方根を求め表示する
    print( math.sqrt(i) )
    #カウンターの平方根を求め表示する
    print( math.pow(i , 1 / 3))
    #1~3の乱数を生成する
    a = random.randint(1,3)
    print( a )
    #sleepは引数で指定された時間
    time.sleep( 1 )
    pass

else:
    print( "end" )