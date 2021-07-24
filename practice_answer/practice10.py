students_scores = []
#配列の準備
students_scores.append([60, 80]) #Aさんのデータを追加
students_scores.append([70, 90]) #Bさんのデータを追加
students_scores.append([80, 100]) #Cさんのデータを追加
students_scores.append([50, 70]) #Dさんのデータを追加
students_scores.append([60, 60]) #Eさんのデータを追加

m = 0
e = 0

for v in students_scores:
    m = m + v[0]
    e = e + v[1]

print("数学の平均点", m / len(students_scores))
print("英語の平均点", e / len(students_scores))