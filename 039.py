from lib import pythagoreanTriples
from itertools import takewhile

def main(limit):
	mem = [0] * (limit + 1)
	for a, b, c in takewhile(lambda t: sum(t) <= limit, pythagoreanTriples()):
		mem[a + b + c] += 1
	return max((m, i) for i, m in enumerate(mem))[1]

print(main(1000)) # 840
