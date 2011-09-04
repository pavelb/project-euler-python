from itertools import count

def A(n):
	if n % 2 == 0 or n % 5 == 0: return 0
	for k in count(1):
		# if R(k) = (10^k - 1)/9 == 0 (mod n)
		if pow(10, k, 9 * n) == 1:
			return k

def p129(limit):
	for n in count(limit):
		if A(n) > limit:
			return n

print(p129(10 ** 6))
