def triples(limit, a = 3, b = 4, c = 5):
	# generate all pythagorean triplets with perimiter <= limit
	# en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
	kmax = limit // (a + b + c)
	if kmax == 0: return
	for k in range(1, kmax + 1):
		yield k*a, k*b, k*c
	for t in triples(limit, a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c):
		yield t
	for t in triples(limit, a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c):
		yield t
	for t in triples(limit, -a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c):
		yield t

def main(n):
	for a, b, c in triples(n):
		if a + b + c == n:
			return a*b*c

print(main(1000))