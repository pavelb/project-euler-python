from lib import multiply, digits
from itertools import combinations

def palindrome(n):
	d = list(digits(n))
	return all(d[i] == d[-1 - i] for i in range(len(d) // 2 + 1))

def main(n, k):
	return max(filter(palindrome, map(multiply, combinations(range(pow(10, k - 1), pow(10, k)), n))))

print(main(2, 3)) # 906609
