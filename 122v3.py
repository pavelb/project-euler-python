# not finished

def snm(n):
	if n <= 1: return 0
	if n % 2 == 0: return 1 + snm(n // 2)
	return 1 + snm(n - 1)

def sumProperDivisors(bitfield, ones, depth, maxn, lowest):
	#prune
	if ones - 1 + depth >= lowest:
		return lowest
	#pop last bit
	n = maxn
	while bitfield[n] == 0:
		n -= 1
	bitfield[n] = 0
	ones -= 1
	#check if done
	if n == 1:
		return depth
	#fan out
	depth += 1
	maxn -= 1
	for a in range(1, n // 2 + 1):
		b = n - a
		abit = bitfield[a]
		bbit = bitfield[b]
		bitfield[a] = 1
		bitfield[b] = 1
		lowest = min(lowest, sumProperDivisors(bitfield, ones + (a > 1 and not abit) + (b > 1 and not bbit), depth, maxn, lowest))
		bitfield[a] = abit
		bitfield[b] = bbit
	bitfield[n] = 1
	return lowest

def m(n):
	bitfield = [0] * (n + 1)
	bitfield[n] = 1
	return sumProperDivisors(bitfield, 1, 0, n, snm(n))

def p122(n):
	return sum(m(i) for i in range(1, n + 1))

#print(p122(200))
#print(m(199))

for k in range(1, 50):
	print(k, m(k))
