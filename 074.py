from lib import digits
from math import factorial

def nonRepeatLen(n):
	mem = set()
	while n not in mem:
		mem.add(n)
		n = sum(map(factorial, digits(n)))
	return len(mem)

def main(limit):
	return sum(nonRepeatLen(n) == 60 for n in range(limit))

print(main(10 ** 6)) # 402
