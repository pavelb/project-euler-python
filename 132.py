from lib import Primes

primes = Primes()

def isFactor(e, p):
	# return (10^e - 1) / 9 == 0 mod p
	# return (10^e - 1) / 9 == kp
	# return 10^e - 1 == k9p
	# return 10^e == 1 + k9p
	# return 10^e == 1 mod 9p
	return pow(10, e, 9 * p) == 1

def main(e, target):
	factors = []
	for p in primes.gen():
		if len(factors) == target:
			break
		i = 1
		while isFactor(e, pow(p, i)):
			factors.append(p)
			i += 1
	return sum(factors)

if __name__ == '__main__':
	print(main(10 ** 9, 40))  # 843296
