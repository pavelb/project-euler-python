from lib import pythagoreanTriples
from itertools import takewhile

def main(limit):
	mem = [0] * (limit + 1)
	perims = map(sum, pythagoreanTriples())
	perims = takewhile(lambda p: p <= limit, perims)
	for p in perims:
		mem[p] += 1
	return max(range(limit + 1), key=lambda i: mem[i])

if __name__ == '__main__':
	print(main(1000)) # 840
