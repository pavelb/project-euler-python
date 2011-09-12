<<<<<<< HEAD
from lib import Primes
from itertools import count

primes = Primes()

def main(limit, target):
	mem = []
	for n in count():
		if sum(1 for _ in primes.factors(n)) == target:
			mem.append(n)
			if len(mem) == limit:
				return mem[0]
		else:
			mem = []

print(main(4, 4)) # 134043
=======
from lib import Primes
from itertools import count

primes = Primes()

def main(limit, target):
	mem = []
	for n in count():
		if len(list(primes.factors(n))) == target:
			mem.append(n)
			if len(mem) == limit:
				return mem[0]
		else:
			mem = []

print(main(4, 4)) # 134043
>>>>>>> upstream/master
