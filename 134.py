from lib import extendedGCD, numLen, Primes
from itertools import takewhile, islice, tee, starmap

primes = Primes()

def S(p1, a):
	b = int(10 ** numLen(p1))
	x, _ = extendedGCD(a, b)
	x *= p1
	# y *= p1
	t = x // b
	x -= t * b
	# y += t * a
	return a * x

def main():
	pr = takewhile(lambda p: p < (10 ** 6 + 4), primes.gen())
	pr1, pr2 = tee(pr, 2)
	pr1 = islice(pr1, 2, None)
	pr2 = islice(pr2, 3, None)
	return sum(starmap(S, zip(pr1, pr2)))

if __name__ == '__main__':
	print(main()) # 18613426663617118
