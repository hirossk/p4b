class Person:
    pass

a = Person()
b = Person()
#クラス名の後に変数を記述するとクラス変数となる。
Person.x = 10
#また実体の__class__を利用するとクラス変数となる。
b.__class__.x = 20
#凡例class-1と同じ書き方ですが、それぞれクラス変数と解釈されると
#実体１と実体２で共通の値を参照していることがわかります。
print("a.x = ", a.x)
print("b.x = ", b.x)