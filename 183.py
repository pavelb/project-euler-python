from lib import gcd
import math

def D(N):
	# d/dk((N/k)^k) = 0 -> k=N/2
	k = int(N / math.e + 0.5)
	# Check if N/k is a terminating decimal
	# Reduce by gcd
	k //= gcd(N, k)
	# Reduce by terminating decimal divisors
	while k % 2 == 0: k //= 2
	while k % 5 == 0: k //= 5
	return N if k > 1 else -N

def main(limit):
	return sum(D(N) for N in range(5, limit + 1))

if __name__ == '__main__':
	print(main(10 ** 4)) # 48861552
