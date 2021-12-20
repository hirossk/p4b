for x in range(1,10): #外ループ
    print(" {:>2d} 行 ".format( x ), end = "") 
    #xの値を出力
    #書式を指定して出力するためには
    for y in range(1,10): #内ループ
        #yの値を出力
        print(" {:>2d}".format(x * y), end = "")
        #printは改行するが、改行を禁止するためにはprintの引数に
        #end = ""を記入する
    print()

