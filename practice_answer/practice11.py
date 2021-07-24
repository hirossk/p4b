subjects = ["Mathematics" ,"English","Social","Japanese","Scientific"]
scores = []
for n in range(3):
    print(n + 1, "人目の入力")
    scores.append([])
    for s in subjects:
        x = input( s + " = " )
        y = int ( x )
        if y > 100 or y < 0 :
            y = -1
            print ( "error" )
        scores[n].append( y )
s_l = len(subjects) #科目数の取得

for m in range(s_l):
    sum = 0
    m_l = len(scores) #人数の取得
    for n in range(m_l):
        sum = sum + scores[n][m]
    print(subjects[m] , "の平均点", sum / 3)