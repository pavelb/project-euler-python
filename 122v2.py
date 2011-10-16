# not finished

def snm(n):
	if n <= 1: return 0
	if n % 2 == 0: return 1 + snm(n // 2)
	return 1 + snm(n - 1)

def sumProperDivisors(bitfield, ones, maxn, depth, lowest):
	#print(bitfield, ones, depth, lowest)
	if ones - 1 + depth >= lowest:
		return lowest
	# pop bit
	n = maxn
	while n > 0:
		if bitfield[n] == 1:
			bitfield[n] = 0
			ones -= 1
			break
		n -= 1
	if n == 1:
		return depth
	depth += 1
	maxn -= 1
	for a in range(1, n // 2 + 1):
		b = n - a
		bitfield2 = list(bitfield)
		ones2 = ones
		if bitfield2[a] == 0:
			bitfield2[a] = 1
			ones2 += 1
		if bitfield2[b] == 0:
			bitfield2[b] = 1
			ones2 += 1
		lowest = min(lowest, sumProperDivisors(bitfield2, ones2, maxn, depth, lowest))
	return lowest

def main(n):
	bitfield = [0] * (n + 1)
	bitfield[n] = 1
	return sumProperDivisors(bitfield, 1, n, 0, snm(n))

print(main(15))
