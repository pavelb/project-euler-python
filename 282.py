# not finished

def A(m, n):
	print(m, n)
	if m == 0: return (n + 1)
	if m == 1: return (2 + (n + 3) - 3)
	if m == 2: return (2 * (n + 3) - 3)
	if m == 3: return (2 ** (n + 3) - 3) % 14 ** 8
	if m > 0 and n == 0: return A(m - 1, 1)
	if m > 0 and n > 0: return A(m - 1, A(m, n - 1))

print(A(4, 3))
