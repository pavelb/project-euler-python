from itertools import count

def pythagoreanTriples(a = 3, b = 4, c = 5):
	# return a generator for the triplets in order of increasing perimiter
	# en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
	yield a, b, c
	gens = [
		((k * a, k * b, k * c) for k in count(2)),
		pythagoreanTriples(a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
		pythagoreanTriples(a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
		pythagoreanTriples(-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
	]
	opts = [(sum(v), v, i) for i, v in enumerate(map(next, gens))]
	while True:
		_, tuple, i = min(opts)
		yield tuple
		tuple = next(gens[i])
		opts[i] = (sum(tuple), tuple, i)

def main(n):
	return next(a * b * c for a, b, c in pythagoreanTriples() if a + b + c == n)

print(main(1000))