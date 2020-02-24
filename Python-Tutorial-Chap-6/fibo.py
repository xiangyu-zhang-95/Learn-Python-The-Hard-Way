import script_1

def fibo(n):
	a, b = 0, 1
	while a < n:
		print(a, end= " ")
		a, b = b, a + b
	print()

def fibo_2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

def _fibo_3(n):
	fibo(n)

