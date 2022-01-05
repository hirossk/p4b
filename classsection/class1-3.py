class Student: 
    #数学の点数を管理する処理
    def set_m(self,m):
        #第二引数は17行目以降のset_mの引数となり
        #実体のデータmとして管理・操作できるように保存
        self.m = m
        if m >= 50:
            #合否を実体のデータgradingとして設定
            self.grading = "good"
        else:
            self.grading = "bad"

a = Student()
b = Student()
c = Student()
#Studentの中身を知らなくてもset_mが何をするのか知っていればOK
a.set_m(75)
b.set_m(48)
c.set_m(95)
print("a ", a.m ,a.grading)
print("b ", b.m ,b.grading)
print("c ", c.m ,c.grading)