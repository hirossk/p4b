json_data = {
  "class":"2年3組" ,
  "name":"佐々木" ,
  "score":[60, 70 ,50 , 80, 100]
  }
  
print('json_data["name"] ⇒ ' +json_data['name'])
print('json_data["score"] ⇒ ' + str(json_data['score']))
print('json_data["score"][1] ⇒ ' + str(json_data['score'][1]))

total = 0
for score in json_data['score']:
	total = total + score
print("平均点:" + str(total/5)) 