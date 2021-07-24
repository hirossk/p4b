#グローバル変数（配列）の準備
subjects = ["Mathematics" ,"English","Social","Japanese","Scientific"]
scores = []
#関数input_dataの記述
def input_data():
    for n in range(3):
        cnt = 0
        scores.append([])
        name = input("Name = ")
        scores[n].append(name)
        for s in subjects:
            x = input( s + " = " )
            y = int ( x )
            if y > 100 or y < 0 :
                y = -1
                print ( "error score" )
            else:
                cnt = cnt + 1
            scores[n].append( y )
        scores[n].append(cnt)
#関数get_averageの記述
def get_average(m):
    sum = 0
    for n in range(1,6):
        if scores[m][n] != -1:
            sum = sum + scores[m][n]
    return sum / scores[m][6]

#プログラムはここから開始
input_data()
for m in range(3):
    ave = get_average(m)
    print(scores[m][0],"の",scores[m][6],"科目の平均点",ave)