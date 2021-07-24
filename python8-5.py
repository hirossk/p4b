def evaluation(score):
    if score < 0 or score > 100:
        mes = "error"
    elif score >= 80:
        mes = "excelent"
    elif score >= 60:
        mes = "good"
    elif score >= 40:
        mes = "passing"
    else:
        mes = "failing"
    return mes

subjects = ["Mathematics" ,"English","Social","Japanese", \
			"Scientific"]
scores = []
for s in subjects:
    x = input( s + " = " )
    y = int ( x )
    scores.append( y )
for n in range(5):
    mes = evaluation(scores[n])
    print ( subjects[n] + ":" , scores[n], mes )