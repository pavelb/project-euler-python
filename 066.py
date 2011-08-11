from math import sqrt

def square(n):
	rootn = sqrt(n)
	return rootn == int(rootn)

def CFR(n):
	def walk(m, d, a, S):
		yield m, d, a, S
		mn = d * a - m
		dn = (S - mn * mn) / d
		an = int((sqrt(S) + mn) / dn)
		for c in walk(mn, dn, an, S):
			yield c
	if not square(n):
		for w in walk(0, 1, int(sqrt(n)), n):
			yield w

def reduce(a, d):
	c, b = d
	return a * c + b, c

def convergents(gen):
	_, _, an, _ = next(gen)
	yield an, 1
	for c in convergents(gen):
		yield reduce(an, c)

def minX(D):
	for x, y in convergents(CFR(D)):
		if x * x - D * y * y == 1: 
			return x
	return float('-inf')

def main(limit):
	return max((minX(D), D) for D in range(2, limit + 1))[1]

print(main(1000))