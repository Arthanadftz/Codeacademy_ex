#Array sorting algorythms
def insert_sort(A):
	""" Sortring A list by inserting """
	N = len(A)
	for top in range(1, N):
		k = top
		while k > 0 and A[k-1] > A[k]:
			A[k], A[k-1] = A[k-1], A[k]
			k -= 1

def choise_sort(A):
	""" Sortring A list by choise """
	N = len(A)
	for pos in range(N-1):
		for k in range(pos+1, N): 
			if A[k] < A[pos]:
				A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
	""" Sortring A list by buble method """
	N = len(A)
	for bypass in range(1, N):
		for k in range(0, N-bypass):
			if A[k] > A[k+1]:
				A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_argotyrhm):
	print("Testing: ", sort_argotyrhm.__doc__)
	print("Testcase #1: ", end='')
	A = [4, 2, 5, 1, 3]
	A_sorted = [1, 2, 3, 4, 5]
	sort_argotyrhm(A)
	print('OK' if A == A_sorted else 'Fail')

	print("Testcase #2: ", end='')
	A = list(range(10, 20)) + list(range(10))
	A_sorted = list(range(20))
	sort_argotyrhm(A)
	print('OK' if A == A_sorted else 'Fail')

	print("Testcase #1: ", end='')
	A = [4, 2, 4, 2, 3]
	A_sorted = [2, 2, 3, 4, 4]
	sort_argotyrhm(A)
	print('OK' if A == A_sorted else 'Fail')

if __name__ == '__main__':
	test_sort(insert_sort)
	test_sort(choise_sort)
	test_sort(bubble_sort)