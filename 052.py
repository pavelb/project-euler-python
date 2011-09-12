<<<<<<< HEAD
from lib import digitCountMap, same
from itertools import count

def main(limit):
	facs = range(1, limit + 1)
	good = lambda n: n > 0 and same(map(digitCountMap, (f * n for f in facs)))
	return next(filter(good, count()))

print(main(6)) # 142857
=======
from lib import digitCountMap, same
from itertools import count

def main(limit):
	facs = range(1, limit + 1)
	return next(n for n in count(1) if same(map(digitCountMap, (f * n for f in facs))))

print(main(6)) # 142857
>>>>>>> upstream/master
