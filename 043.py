from lib import num
from itertools import permutations

def main():
	primes = (2, 3, 5, 7, 11, 13, 17)
	good = lambda k: all(num(k[i + 1:i + 4]) % p == 0 for i, p in enumerate(primes))
	pandigitals = permutations(range(10))
	return sum(map(num, filter(good, pandigitals)))

if __name__ == '__main__':
	print(main()) # 16695334890
