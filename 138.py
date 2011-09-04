from lib import convergents
from itertools import islice

def goodConvergentsOf(D):
	for x, y in convergents(D):
		if x > 2 and x * x - D * y * y == -1:
			yield x, y

def solutions():
	# (b/2)^2 + (b+-1)^2 = L^2		=>		(5*b/2+-2)^2 - 5L^2 = -1
	# the solutions are the convergents of the Pell equation x^2 - 5*L^2 = -1
	for x, L in goodConvergentsOf(5):
		if (x - 2) % 5 == 0 or (x + 2) % 5 == 0: # (2 * (x - 2) // 5) or (2 * (x + 2) // 5)
			yield L

def main(limit):
	return sum(islice(solutions(), limit))

print(main(12)) # 1118049290473932
