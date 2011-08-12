from lib import num
from itertools import permutations

def main():
	primes = (2, 3, 5, 7, 11, 13, 17)
	good = lambda digits: all(num(digits[i + 1:i + 4]) % p == 0 for i, p in enumerate(primes))
	return sum(map(num, filter(good, permutations(range(10)))))

print(main()) # 16695334890
