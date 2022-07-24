subjects = ["Mathematics" ,"English","Social","Japanese","Scientific"]
scores = []
for s in subjects:
    x = input( s + " = " )
    y = int ( x )
    if y > 100 or y < 0 :
        y = -1
        print ( "error" )
    scores.append( y )

for n in range(0,5):
    if scores[n] == -1:
        mes = "error"
    elif scores[n] >= 80:
        mes = "excelent"
    elif scores[n] >= 60:
        mes = "good"
    elif scores[n] >= 40:
        mes = "passing"
    else:
        mes = "failing"
    print ( subjects[n] + ":" , scores[n], mes )