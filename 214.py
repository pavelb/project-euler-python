from lib import numLen, Primes
from collections import defaultdict

prime = Primes()

class chainLenObj():
	def __init__(self, limit):
		self.limit = limit
		self.mem = [None] * limit
		self.mem[1] = 1

	def get(self, n):
		if self.mem[n] == None:
			self.mem[n] = 1 + self.get(prime.phi(n))
		return self.mem[n]

	def gen(self, length):
		for p in prime.gen():
			if p >= self.limit:
				break
			print(p)
			if self.get(p) == length:
				yield p

def main(limit, length):
	clo = chainLenObj(limit)
	return sum(clo.gen(length))

# brute force, takes forever
if __name__ == '__main__':
	print(main(40000000, 25))  # 1677366278943
