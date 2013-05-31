from lib import Primes

primes = Primes()

def main(n):
	return max(b for b, _ in primes.factors(n))

if __name__ == '__main__':
	print(main(600851475143)) # 6857
