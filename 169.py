def fusc2(n):
	if n <= 0: return 0
	if n == 1: return 1
	if n & 1 == 0: return fusc(n >> 1)
	t = (n - 1) >> 1
	return fusc(t) + fusc(t + 1)

def fusc(n):
	a = 1
	b = 0
	while n:
		if n & 1:
			b += a
		else:
			a += b
		n >>= 1
	return b

print(fusc(10 ** 25 + 1))
