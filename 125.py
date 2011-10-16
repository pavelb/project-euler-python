# not finished

def ss(m, n): return (n * (n + 1) * (2 * n + 1) - m * (m - 1) * (2 * m - 1)) / 6

def isPalin(n):
	s = str(n)
	return s == s[::-1]

def p125(limit):
	hist = dict()
	for n in xrange(2, int(limit ** 0.5)):
		for m in xrange(n - 1, 0, -1):
			s = ss(m, n)
			if s < limit: break
			if isPalin(s): hist[s] = True
	return sum(hist.keys())

print(p125(10 ** 8))
