import math

def gcd(a, b):
	while b != 0: a, b = b, a % b
	return a

def D(N):
	k = int(N / math.e + 0.5)
	k /= gcd(N, k)
	while k % 2 == 0: k /= 2
	while k % 5 == 0: k /= 5
	return N if k > 1 else - N

def p183(limit): return sum(D(N) for N in xrange(5, limit + 1))

print(p183(10 ** 4))
