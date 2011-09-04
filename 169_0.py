def main(n):
	n += 1
	a = 1
	b = 0
	while n:
		if n & 1:
			b += a
		else:
			a += b
		n >>= 1
	return b

print(main(10 ** 25))
