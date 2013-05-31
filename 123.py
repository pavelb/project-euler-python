from lib import Primes

primes = Primes()

def main(limit):
	n = 0
	for p in primes.gen():
		n += 1
		if n % 2 == 1 and 2 * n * p > limit:
			return n

if __name__ == '__main__':
	print(main(10 ** 10)) # 21035
