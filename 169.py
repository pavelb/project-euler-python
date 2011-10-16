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

def main(n):
	return fusc(n)

print(main(10 ** 25 + 1)) # 178653872807
