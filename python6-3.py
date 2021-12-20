subjects = ["Mathematics","English","Social",
    "Japanese","Scientific"]
scores = [] 
for s in subjects:
    x = input( s + " = " )
    y = int ( x )
    scores.append( y )

for n in range(0,5):
    if scores[n] >= 60:
        mes = "合格"
    else:
        mes = "不合格"
    print ( subjects[n] + ":" , scores[n], mes)