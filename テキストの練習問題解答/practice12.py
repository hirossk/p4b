def func1(n):
    a = (n - 65)**2
    return a

def func2():
    t = 0
    for i in range(5):
        x = input(str(i + 1) + "人目の点数")
        y = int(x)
        t = t + func1(y)
    return t

z = func2()
print( z / 5 )