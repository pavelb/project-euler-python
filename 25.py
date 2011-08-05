def main(limit):
	n = 0
	a, b = 0, 1
	while len(str(a)) < limit:
		n += 1
		a, b = b, a + b
	return n

print(main(1000))