from itertools import count

def primes(limit = float('inf')):
	prim = list()
	for n in count(2):
		if n > limit: return
		good = True
		for p in prim:
			if p * p > n: break
			if n % p == 0:
				good = False
				break
		if good:
			prim.append(n)
			yield n

def main(n):
	i = 0
	for p in primes():
		i += 1
		if i == n:
			return p

print(main(10001))