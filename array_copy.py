N = int(input("Введите размер массива: "))
A = [0]*N
B = [0]*N
print(A)
print(B)

for i in range(N):
	x = int(input('Введите число: '))
	A[i] = x

print(A)

for i in range(N):
	B[i] = A[i]

print(B)
