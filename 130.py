from itertools import count
from lib import gcd, Primes

primes = Primes()

def A(n):
    return next(k for k in count(1) if pow(10, k, 9 * n) == 1)

def main(limit):
    rv = 0
    for n in count(3):
        if gcd(n, 10) != 1:
            continue
        if primes.isPrime(n):
            continue
        if (n - 1) % A(n) != 0:
            continue
        rv += n
        limit -= 1
        if limit == 0:
            return rv

if __name__ == '__main__':
	print(main(25))  # 149253
