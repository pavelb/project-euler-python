# not finished

def gen(n):
	singleton = set([n])
	if n == 1:
		yield singleton
	else:
		for a in range(1, n // 2 + 1):
			for left in gen(a):
				tmp = singleton.union(left)
				for right in gen(n - a):
					yield tmp.union(right)

def m(k):
	op = min(gen(k), key=len)
	op.remove(1)
	return k, len(op), sorted(list(op))

for k in range(1, 200):
	print(m(k))
