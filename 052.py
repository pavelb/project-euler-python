from lib import digitCountMap, same
from itertools import count

def main(limit):
	# trick: want the digits of 2x, 3x, ... to equal
	# if limit > 2 we must have 2x = 3x mod 9 or x = 0 mod 9
	skip = 1 if limit < 3 else 9
	facs = range(2, limit + 1)
	good = lambda n: n > 0 and same(map(digitCountMap, (f * n for f in facs)))
	return next(filter(good, count(0, skip)))

if __name__ == '__main__':
	print(main(6)) # 142857
