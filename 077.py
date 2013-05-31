from lib import Primes, runningSum
from itertools import count, takewhile

primes = Primes()

def partitionFnGen(): # partition function over the primes
	mem = [[1]]

	def get(n, i): # in how many ways can n be written using primes of index >= i
		if n == 0: return 1
		if n < primes.get(i): return 0
		return mem[n][i]

	for n in count(1):
		parts = takewhile(lambda p: p <= n, primes.gen())
		decomp = [get(n - p, i) for i, p in enumerate(parts)]
		mem.append(list(reversed(list(runningSum(reversed(decomp))))))
		yield get(n, 0)

def main(limit):
	return next(i + 1 for i, p in enumerate(partitionFnGen()) if p > limit)

if __name__ == '__main__':
	print(main(5000)) # 71
