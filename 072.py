from lib import Primes

primes = Primes()

def main(limit):
	# trick: count the number of potential numerators for all denominators
	return sum(map(primes.phi, range(2, limit + 1)))

if __name__ == '__main__':
	print(main(10 ** 6)) # 303963552391
