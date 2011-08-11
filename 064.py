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

def period(iterable):
	hist = set()
	for i, item in enumerate(iterable):
		if item in hist:
			return i - 1
		hist.add(item)
	return 0

def main(lim):
	return sum(period(CFR(n)) % 2 for n in range(2, lim + 1))

print(main(10000))