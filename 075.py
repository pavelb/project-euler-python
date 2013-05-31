from itertools import takewhile, groupby
from lib import pythagoreanTriples

def main(lim):
	# trick: generate the triples in order of increasing perimeter, check adjacent perimeters for differences
	perimeters = map(sum, pythagoreanTriples())
	perimeters = takewhile(lambda L: L <= lim, perimeters)
	return sum(sum(1 for _ in g) == 1 for _, g in groupby(perimeters))

if __name__ == '__main__':
	print(main(1500000)) # 161667
