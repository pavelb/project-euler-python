from lib import Primes

primes = Primes()

def divisors(n):
	rv = [1]
	for f, e in primes.factors(n):
		rv.extend([r * f ** i for i in range(1, e + 1) for r in rv])
	return rv

def count(t):
	if t % 4: return 0
	rt = t // 4
	roott = t ** 0.5
	rootrt = rt ** 0.5
	rv = 0
	for k in sorted(divisors(rt)):
		if k >= rootrt: break
		S = rt // k + k
		if S > roott: rv += 1
	return rv

def main():
	return sum(1 <= count(t) <= 10 for t in range(8, 10 ** 6 + 1, 4))

if __name__ == '__main__':
	print(main()) # 209566
