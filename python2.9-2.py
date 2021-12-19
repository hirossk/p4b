def func1(x):
    answer = x ** 2 + 2 * x + 3
    return answer
#1つ目の関数func1はここまで

def func2(n):
	t = 0
	for i in range(n):
		y = func1(i)
		t = t + y
	return t
#2つ目の関数func2はここまで

a = func2(5)
print( a )