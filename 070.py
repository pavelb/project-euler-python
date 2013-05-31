from lib import digitCountMap, Primes
from itertools import takewhile

primes = Primes()

def main(limit):
	# trick: to maximize phi(n) need n to be a product of two primes, as it can't be prime itself
	minn, minphi = 1, -1
	for p1 in primes.gen():
		if p1 * 3 >= limit:
			break
		p2lim = min(p1, limit / p1)
		for p2 in takewhile(lambda p: p < p2lim, primes.gen()):
			n = p1 * p2
			phi = (p1 - 1) * (p2 - 1)
			if n * minphi < minn * phi and digitCountMap(n) == digitCountMap(phi):
				minn, minphi = n, phi
	return minn

if __name__ == '__main__':
	print(main(10 ** 7)) # 8319823
