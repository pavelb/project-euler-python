from lib import multiply
from itertools import combinations

def palindrome(n):
	s = str(n)
	return s == s[::-1]

def main(n, k):
	prods = (multiply(c) for c in combinations(range(pow(10, k)), n))
	return max(p for p in prods if palindrome(p))

print(main(2, 3))