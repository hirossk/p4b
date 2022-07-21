# JSONデータをリストの中の辞書データとして格納します
# 形式をみるとリストの中に辞書データが複数含まれています

jsondata = [
{"City":"夕張市","Tree":"サクラ","Flower":"ツツジ"},
{"City":"岩見沢市","Tree":"コブシ","Flower":"バラ"},
{"City":"美唄市","Tree":"ポプラ","Flower":"ツツジ"},
{"City":"芦別市","Tree":"ミズナラ","Flower":"ユリ"},
{"City":"赤平市","Tree":"カエデ","Flower":"キク"},
{"City":"三笠市","Tree":"ナナカマド","Flower":"キク"},
{"City":"滝川市","Tree":"プラタナス","Flower":"ツツジ、コスモス"}
]

# データの中身を確認します
#print(jsondata)
# dictdataそのものはリストの形式なのでここから2番目の要素を
# 出力します
#print(jsondata[2])
# 一度2番目の要素を変数dictdataに代入します
#dictdata = jsondata[2]

# jsondataのデータ型とdictdataのデータ型を表示する
# ためにtype関数を使います
#print('jsondataの型は', type(jsondata))
#print('dictdataの型は', type(dictdata))

# 探索用の空リストを作成します
#listdata = []
# リスト内の全データから'Cityを取得しlistdataに格納します
#for data in jsondata:
#    listdata.append(data['City'])
# リストから滝川市の要素番号を取得します
#i = listdata.index('滝川市')
# 滝川市の木の名称をdictdataから取得します
#print('滝川市の木=',jsondata[i]['Tree'])