from lib import digitCountMap, same
from itertools import count

def main(limit):
	facs = range(1, limit + 1)
	good = lambda n: n > 0 and same(map(digitCountMap, (f * n for f in facs)))
	return next(filter(good, count()))

if __name__ == '__main__':
	print(main(6)) # 142857
