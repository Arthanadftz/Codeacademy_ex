N = int(input('Введите число, факториал которого небходимо вычислить'))
def factorial(N):
	assert N >= 0, 'Факториал отрицальных чисел не допустим в данном алгоритме.'
	if N == 0:
		return 1
	return factorial(N-1)*N

print('Факториал %s равен: %s' %(N, factorial(N)))


N1 = int(input('Введите конечное число последовательности Фиббоначчи: '))
def fib(N1):
	assert N1 >= 0, 'Последовательность Фиббоначчи начинается с 0.'
	a = 0
	b = 1
	for __ in range(N1):
		a, b = b, a + b
		print(a, "%s - итерация." %(__))
	return a

fib(N1)
