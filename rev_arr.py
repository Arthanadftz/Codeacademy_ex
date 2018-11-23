N = int(input('Введите размер массива: '))
A = [0]*N
for i in range(N):
	x = int(input('Введите элемент массива: '))
	A[i] = x

print(A)

def reverse_array(A, N):
	for i in range(N//2):
		A[i], A[N-1-i] = A[N-1-i], A[i]
	return A

reverse_array(A, N)
print(A)


def test_rev_arr():
	A1 = [1, 2, 3, 4, 5]
	if reverse_array(A1, 5) == [5, 4, 3, 2, 1]:
		print('Test1 - Ok')
	else:
		print('Test1 fail')
	A2 = [1, 2, 3, 4, 5, 6]
	if reverse_array(A2, 6) == [6, 5, 4, 3, 2, 1]:
		print('Test2 - Ok')
	else:
		print('Test2 fail')
	if reverse_array(A2, 6) == [1, 2, 3, 4, 5, 6]:
		print('Test3 fail')
	else:
		print('Test3 - ok')

test_rev_arr()
