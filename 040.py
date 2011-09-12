<<<<<<< HEAD
from lib import multiply, digits
from itertools import count

def blockLen(k): # start index of 10^(n-1) in concatenation of all padded k-digit numbers
	return pow(10, k - 1) * k

def startIndex(n): # start index of 10^(n-1) in concatenation of all numbers
	return blockLen(n) - (pow(10, n) - 10) // 9

def pd(n, k): # nth digit in concatenation of all padded k-digit numbers
	q, r = divmod(n, k)
	return digits(q)[r]

def d(n): # nth digit in concatenation of all numbers
	k = next(k for k in count(1) if n < startIndex(k + 1))
	# we know the index is in a seq of k-digit numbers starting at 10^(k-1)
	n -= startIndex(k) # start indexing at the 1 in 10^(k-1)
	n += blockLen(k) # start indexing at [0]^k by accounting for missing block 0[0-9]^(k-1)
	return pd(n, k)

def main(indices):
	return multiply(map(d, indices))

print(main([1, 10, 100, 1000, 10000, 100000, 1000000])) # 210
=======
from lib import multiply
from itertools import count

def blockLen(k): # start index of 10^(n-1) in concatenation of all padded k-digit numbers
	return pow(10, k - 1) * k

def startIndex(n): # start index of 10^(n-1) in concatenation of all numbers
	return blockLen(n) - (pow(10, n) - 10) // 9

def pd(n, k): # nth digit in concatenation of all padded k-digit numbers
	if k == 1:
		return n
	blen = blockLen(k)
	if n % k == 0:
		return n // blen # leading digit
	n %= blen # account for cycling
	skip = 1 + n // k # skip all i where i % k == 0
	return pd(n - skip, k - 1)

def d(n): # nth digit in concatenation of all numbers
	k = next(k for k in count(1) if n < startIndex(k + 1))
	# we know the index is in a seq of k-digit numbers starting at 10^(k-1)
	n -= startIndex(k) # start indexing at the 1 in 10^(k-1)
	n += blockLen(k) # start indexing at [0]^k by accounting for missing block 0[0-9]^(k-1)
	return pd(n, k)

def main(indices):
	return multiply(map(d, indices))

print(main([1, 10, 100, 1000, 10000, 100000, 1000000])) # 210
>>>>>>> upstream/master
