from itertools import count

def p207(limit):
	# k = (2^t)^2 - 2^t, where 2^t is an integer
	# hence t = log2(n), n integer
	# hence k = n^2 - n
	perfect = 0
	for n in count(2):
		if n & (n - 1) == 0:
			perfect += 1
		elif perfect < limit * (n - 1):
			return n * (n - 1)

print(p207(1.0 / 12345))
