# This code is a complete mess and needs to be redone

def p122_1(base):
	db = [None] * base
	db[1] = [set([1])]

	for n in range(2, base):
		db[n] = []
		for a in range(1, n // 2 + 1):
			b = n - a
			bv = set([n, a, b])
			for set1 in db[a]:
				for set2 in db[b]:
					db[n].append(bv.union(set1, set2))
		s = sorted(db[n], key=len)
		print(n, len(s[0]) - 1)

def p122_2(base):
	def gen(n):
		if n <= 1:
			yield set([1])
		else:
			for a in range(1, n // 2 + 1):
				b = n - a
				s = set([n, a, b])
				for c in gen(a):
					for d in gen(b):
						yield s.union(c, d)
	for n in range(1, base):
		best = min(gen(n), key=len)
		print(n, len(best) - 1, best)

def p122_3(base):
	from math import ceil

	def getMin(iterable):
		return min(iterable, key=len)

	def pp(db, i):
		s = getMin(db[i])
		print(i, len(s) - 1, len(db[i]), s)

	db = [[] for _ in range(base)]
	db[1] = [set([1])]

	for i in range(1, ceil(base / 2)):
		for j in range(i, base - i):
			m = i + j # 2 * i <= m < base
			sets = (set([m]).union(a).union(b) for a in db[i] for b in db[j])
			if m >= base - i: # can NOT be used as a part
				db[m] = [getMin(sets)]
			else:
				db[m].extend(sets)
		db[i] = [getMin(db[i])]
	for i in range(1, base):
		pp(db, i)

#p122_3(30)
#p122(200)

from math import floor, log
from copy import copy
from heapq import heappush, heappop

def bitCount(n):
	c = 0
	while n > 0:
		n &= n - 1
		c += 1
	return c

def squareAndMultiply(n):
	if n <= 1: return 0
	if n % 2 == 0: return 1 + squareAndMultiply(n // 2)
	return 1 + squareAndMultiply(n - 1)

def squareAndMultiplyBound(n):
	return floor(log(n, 2)) + bitCount(n) - 1

def lowestBound(n):
	return gen([-n], set([]), squareAndMultiply(n))

def gen(input, output, lowest):
	#print(input, output, lowest)
	if len(input) + len(output) >= lowest: return lowest
	if len(input) == 0:
		#print('done', output, lowest)
		return len(output)
	n = -heappop(input)
	output.add(n)
	for a in range(1, n // 2 + 1):
		b = n - a
		newinput = copy(input)
		if a != 1: heappush(newinput, -a)
		if b != 1 and b != a: heappush(newinput, -b)
		lowest = min(lowest, gen(newinput, copy(output), lowest))
	return lowest

print(lowestBound(15))
#print(sum(lowestBound(n) for n in range(1, 200 + 1)))