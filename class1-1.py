class Person:
    pass #なんの命令もない空クラス（型）
    
#実体の作成　１つ目　変数a、二つ目　変数b
a = Person()
b = Person()
#１つ目の実体のxという変数に10を代入
a.x = 10
#２つ目の実体のxという変数に20を代入
b.x = 20
#１つ目aと二つ目bの実体のxという変数を出力 
print("a.x = ", a.x)
print("b.x = ", b.x)