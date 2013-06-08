from lib import multiply, palindrome, num, Primes, digits
from itertools import combinations

primes = Primes()

def palins(arr, size):
	if size == 0:
		yield []
	elif size == 1:
		for a in arr:
			yield [a]
	else:
		for p in palins(arr, size - 2):
			for a in arr:
				yield [a] + p + [a]


def main(k):
	# generate all palindromes of allowed sizes and factor them to see if
	# divisors have correct properties
	def seq(k):
		for m in range(1, k + 4):
			for p in palins(range(10), m):
				if p[0] == 0:
					continue
				n = num(p)
				for d in primes.divisors(n):
					if len(digits(d)) == k and len(digits(n // d)) == k:
						yield n
	return max(seq(k))

if __name__ == '__main__':
	print(main(3)) # 906609
