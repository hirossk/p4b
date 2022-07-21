# JSONモジュールの読み込みをします
import requests

# 地震の発生状況を知るためのデータURLを設定します
url = "https://www.jma.go.jp/bosai/quake/data/list.json"
# データの取得を行います
#data = requests.get(url).json()

# 取得したJSONデータはリスト形式であることを確認します
#print(type(data)
# リストの最初のデータから地域（エリア）を取得します
#print(data[0]['anm'])
# リストの最初のデータから最大震度を取得します
#print(data[0]['maxi'])
# リストから発生地震の詳細データのJSONデータ名を取得します
#print(data[0]['json'])

