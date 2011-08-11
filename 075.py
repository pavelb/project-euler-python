def triples(a, b, c, Ls, lim):
	L = a + b + c
	if L > lim: return
	for i in range(L, lim, L): Ls[i] += 1 #account for multiples
	triples(a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c, Ls, lim)
	triples(a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c, Ls, lim)
	triples(-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c, Ls, lim)
	return Ls

def main(lim):
	return sum(L == 1 for L in triples(3, 4, 5, [0] * lim, lim))

print(main(1500000))