from lib import Primes

primes = Primes()

def main(limit):
	saw = [False] * (limit + 1)

	def cycle(n):
		chain = []
		while n < len(saw) and not saw[n]:
			saw[n] = True
			chain.append(n)
			n = primes.sumDivisors(n)
		return chain[chain.index(n):] if n in chain else []

	cycles = map(cycle, range(1, limit + 1))
	return min(max(cycles, key=len))

if __name__ == '__main__':
	print(main(1000000)) # 14316
