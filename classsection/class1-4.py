class Student: 
    def set_m(self,m):
        self.m = m
        if m >= 50:
            self.grading = "good"
        else:
            self.grading = "bad"
#クラス宣言の括弧の中に利用したい機能のスーパークラスを記載します。
class SubStudent(Student): 
    def set_e(self,e):
        self.e = e
        if e >= 50:
            #合否を実体のデータe_gradingとして設定
            self.e_grading = "good"
        else:
            self.e_grading = "bad"
a = SubStudent()
a.set_m(80)
a.set_e(30)
print("a Mathematics", a.m ,a.grading)
print("a English", a.e ,a.e_grading)