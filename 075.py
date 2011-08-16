from itertools import takewhile, groupby
from lib import pythagoreanTriples

def main(lim):
	# trick: generate the triples in order of increasing perimeter, check adjacent perimeters for differences
	perimeters = takewhile(lambda L: L <= lim, map(sum, pythagoreanTriples()))
	return sum(len(list(g)) == 1 for _, g in groupby(perimeters))

print(main(1500000)) # 161667
