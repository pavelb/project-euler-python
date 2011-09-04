from lib import digits
from itertools import islice
from heapq import heappush, heappop

def seq():
	yield 81
	mem = []
	push = lambda b, e: heappush(mem, (b ** e, b, e))
	push(2, 3)
	while True:
		n, b, e = heappop(mem)
		if b == sum(digits(n)):
			yield n
		if e == 3:
			push(b + 1, 3)
		push(b, e + 1)

def main(n):
	return next(islice(seq(), n - 1, n))

print(main(30)) # 248155780267521
