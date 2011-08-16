from lib import multiply, palindrome
from itertools import combinations

def main(n, k):
	return max(filter(palindrome, map(multiply, combinations(range(pow(10, k - 1), pow(10, k)), n))))

print(main(2, 3)) # 906609
