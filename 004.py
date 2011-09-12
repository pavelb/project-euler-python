from lib import multiply, palindrome
from itertools import combinations

def main(n, k):
<<<<<<< HEAD
	kdigitnums = range(pow(10, k - 1), pow(10, k))
	prods = map(multiply, combinations(kdigitnums, n))
	return max(filter(palindrome, prods))
=======
	return max(filter(palindrome, map(multiply, combinations(range(pow(10, k - 1), pow(10, k)), n))))
>>>>>>> upstream/master

print(main(2, 3)) # 906609
