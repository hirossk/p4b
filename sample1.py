#100点満点でテストした結果をscoreという変数に格納する
#テストの点数が80点以上で優、70点以上で良、60点以上で可、60点未満で不可とする
#ただし入力データのエラー処理は考えない
score = 60

if score >= 80:
    #インデント（字下げ）がされていないとエラーになります
print("あなたは優です")
    #インデント（字下げ）がおかしいとエラーになります
    elif score >= 70:
    print("あなたは良です")
elif score >= 60:
    print("あなたは可です")
else:
    print("あなたは不可です")
