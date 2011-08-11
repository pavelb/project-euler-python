def simplify(a, b):
	return [a, 1] if b[0] == 0 else [b[0] * a + b[1], b[0]]

def gen(i, t = 2, k = 0):
	if i == -2:
		return 0, 0
	if t == 1:
		return simplify(1, gen(i - 1, 2, k))
	if t == 2:
		return simplify(1, gen(i - 1, 3, k))
	if t == 3:
		return simplify(k, gen(i - 1, 1, k + 2))

def main(lim):
	return sum(map(int, str(gen(lim)[0])))

print(main(100))
