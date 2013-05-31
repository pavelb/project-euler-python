from lib import Primes

primes = Primes()

def main(lim):
	return max(range(1, lim), key=lambda n: n / primes.phi(n))

if __name__ == '__main__':
	print(main(1000000)) # 510510
