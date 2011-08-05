def is_prime(n):
	return list(zip((True, False), decompose(n)))[-1][0]

class IsPrimeCached(dict):
	def __missing__(self, n):
		r = is_prime(n)
		self[n] = r
		return r

is_prime_cached = IsPrimeCached()

def primes():
	yield 2
	n = 3
	while 1:
		yield n
		n += 2
		while not is_prime_cached[n]: n += 2

def decompose(n):
	sq = n ** 0.5
	for p in primes():
		if p > sq: break
		while n % p == 0:
			yield p
			n /= p
	if n > 1:
		yield n

def main():
	n = 0
	for p in primes():
		n += 1
		if n % 2 == 0: continue
		r = 2 * n * p % p * p
		if r > 10 ** 10: return n

print(main())
