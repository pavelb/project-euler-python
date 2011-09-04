def u(n):
	return (1 + n ** 11) // (1 + n)

def getA(n):
	return [[b ** e for e in range(n - 1, -1, -1)] for b in range(1, n + 1)]

def getB(n):
	return [u(i) for i in range(1, n + 1)]

def timesc(c, iterable):
	return [c * i for i in iterable]

def minus(A, B):
	return [a - b for a, b in zip(A, B)]

def times(A, B):
	return [a * b for a, b in zip(A, B)]

def printM(M):
	print("[")
	for m in M: print('\t' + str(m))
	print("[")

def down(A, B):
	for i in range(len(A) - 1):
		for j in range(i + 1, len(A)):
			m = A[j][-(i + 1)] // A[i][-(i + 1)]
			A[j] = minus(A[j], timesc(m, A[i]))
			B[j] = B[j] - m * B[i]
	return A, B

def up(A, B):
	for irow in range(len(A) - 1, -1, -1):
		icol = len(A) - 1 - irow
		B[irow] //= A[irow][icol]
		A[irow][icol] = 1
		for jrow in range(irow - 1, -1, -1):
			m = A[jrow][icol]
			A[jrow] = minus(A[jrow], timesc(m, A[irow]))
			B[jrow] = B[jrow] - m * B[irow]
	return A, B

def OP(k, n):
	A = getA(k)
	B = getB(k)
	# solve the system of linear equations Ax = B
	A, B = down(A, B)
	# at this point the matrix looks like
	# a, a, a
	# b, c, 0
	# d, 0, 0
	A, B = up(A, B)
	# at this point the matrix looks like
	# 0, 0, 1
	# 0, 1, 0
	# 1, 0, 0
	return sum(times(B, (n ** i for i in range(k))))

def main(limit):
	return sum(OP(k, k + 1) for k in range(1, limit + 1))

print(main(10)) # 37076114526
