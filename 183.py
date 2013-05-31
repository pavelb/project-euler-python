from lib import gcd
import math

def D(N):
	k = int(N / math.e + 0.5)
	k //= gcd(N, k)
	while k % 2 == 0: k //= 2
	while k % 5 == 0: k //= 5
	return N if k > 1 else -N

def main(limit):
	return sum(D(N) for N in range(5, limit + 1))

if __name__ == '__main__':
	print(main(10 ** 4)) # 48861552
