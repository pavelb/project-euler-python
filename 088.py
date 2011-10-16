from lib import Primes
from itertools import count, chain
from heapq import heappush, heappop

primes = Primes()

def reduce(facs):
	for i, m in enumerate(facs):
		n = facs[:i] + facs[i + 1:]
		for j in range(i, len(facs) - 1):
			yield sorted(n[:j] + [n[j] * m] + n[j + 1:])

def prodSum(n, k):
	# breadth-first search, note that the sum increases as the number of product terms decreases
	states = []
	history = []
	target = n - k

	def push(facs):
		if facs not in history:
			history.append(facs)
			heappush(states, (sum(facs) - len(facs), facs))

	push(list(chain.from_iterable([b] * e for b, e in primes.factors(n))))

	while states:
		diff, facs = heappop(states)
		if diff == target:
			return True
		if diff > target:
			break
		for s in reduce(facs):
			push(s)

	return False

def mps(k):
	return next(n for n in count(k) if prodSum(n, k))

def main(lbound, ubound):
	return sum(set(map(mps, range(lbound, ubound + 1))))

print(main(2, 12000)) # 7587457
