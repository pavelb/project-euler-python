from itertools import count

def tribonacci():
	a, b, c = 1, 1, 1
	while True:
		yield a
		a, b, c = b, c, a + b + c

def main(limit):
	for n in count(1, 2):
		ts = tribonacci()
		m0, m1, m2 = next(ts) % n, next(ts) % n, next(ts) % n
		for t in ts:
			if t % n == 0: # n divides t
				break
			m0, m1, m2 = m1, m2, t % n
			if m0 == m1 == m2: # loop found
				limit -= 1
				if limit <= 0:
					return n
				break

print(main(124)) # 2009
