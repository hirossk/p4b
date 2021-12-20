students_scores = [[60, 80], [70, 90], [80, 100]]
m = 0 #数学の合計点
e = 0 #英語の合計点

for i in range (3):
    m = m + students_scores[i][0]
    e = e + students_scores[i][1]

print ("数学の合計点数", m)
print ("英語の合計点数", e)