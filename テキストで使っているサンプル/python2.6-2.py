subjects = ["Mathematics","English","Social",
    "Japanese","Scientific"]
scores = [] 
#空のリストを作成
for s in subjects:
    x = input( s + " = " )
    y = int ( x )
    scores.append( y )
    #scoresリストに要素（y）を数値として追加する

l = len(subjects)
#配列の長さはlen関数を利用することで求められます（ここでは5となります）
for n in range(l):
    print ( subjects[n] + ":" , scores[n])
# print命令は「,」（カンマ）でつなぐと改行なしで値を出力できます。