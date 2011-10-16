from lib import Primes

primes = Primes()

def main(limit):
	count = 0
	i = 0
	p1 = primes.get(0)
	p1limit = limit // p1
	while p1 <= p1limit:
		j = i
		p2 = primes.get(i)
		p2limit = limit // p1
		while p2 <= p2limit:
			count += 1
			j += 1
			p2 = primes.get(j)
		i += 1
		p1 = primes.get(i)
	return count

print(main(10 ** 8)) # 17427258
