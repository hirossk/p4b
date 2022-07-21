# JSONモジュールの読み込みをします
import json

# JSONファイルを外部ファイルから開きます
jsonfile = open('json/hokkaidotreeflower.json' , 'r', encoding='utf-8') 
# JSONデータとして取り出します
loaded_data = json.load(jsonfile)  

# 全データから目的のデータを探します
#for unitdata in loaded_data:
    # ここでunitデータは各市区町村ごとの一つの辞書データ
    # 辞書から市町村のデータを取り出す
    #print(unitdata['City'])
    # 市町村名が一致するかチェックします
    #if unitdata['City'] == '札幌市':
         # 一致した場合市町村名と木の名前、花の名前を辞書から
         #取り出して出力します
    #    print(unitdata['City'],'の木は',unitdata['Tree'])
    #    print('花は',unitdata['Flower'],'です')
    

