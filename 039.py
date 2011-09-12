<<<<<<< HEAD
from lib import pythagoreanTriples
from itertools import takewhile

def main(limit):
	mem = [0] * (limit + 1)
	perims = map(sum, pythagoreanTriples())
	perims = takewhile(lambda p: p <= limit, perims)
	for p in perims:
		mem[p] += 1
	return max(range(limit + 1), key=lambda i: mem[i])

print(main(1000)) # 840
=======
from lib import pythagoreanTriples
from itertools import takewhile

def main(limit):
	mem = [0] * (limit + 1)
	for a, b, c in takewhile(lambda t: sum(t) <= limit, pythagoreanTriples()):
		mem[a + b + c] += 1
	return max((m, i) for i, m in enumerate(mem))[1]

print(main(1000)) # 840
>>>>>>> upstream/master
