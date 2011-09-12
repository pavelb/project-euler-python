from math import log10, ceil

def cycle(d):
	mem = []
	rv = []
	n = 1
	while n not in mem:
		if n == 0:
			return []
		mem.append(n)
		nn = n * pow(10, ceil(log10(d / n)))
		n = nn % d
		rv.append(nn // d)
	return rv[mem.index(n):]

def main(limit):
<<<<<<< HEAD
	cycleLen = lambda d: len(cycle(d))
	return max(range(2, limit), key=cycleLen)
=======
	return max(range(2, limit), key = lambda d: len(cycle(d)))
>>>>>>> upstream/master

print(main(1000)) # 983
