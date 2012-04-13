from lib import numLen, Primes
from collections import defaultdict

prime = Primes()

class chainLenObj():
	def __init__(self, limit):
		self.limit = limit
		self.mem = [None] * limit
		self.mem[1] = 1

	def get(self, n, definitely_prime):
		rv = self.mem[n]
		if rv != None:
			return rv
		if definitely_prime:
			rv = 1 + self.get(n - 1, False)
		else:
			rv = 1 + self.get(prime.phi(n), False)
		self.mem[n] = rv
		return rv

	def gen(self, length):
		for p in prime.gen():
			if p >= self.limit:
				break
			print(p)
			if self.get(p, True) == length:
				yield p

def main(limit, length):
	clo = chainLenObj(limit)
	return sum(clo.gen(length))

# brute force, takes forever
print(main(40000000, 25))  # 1677366278943
