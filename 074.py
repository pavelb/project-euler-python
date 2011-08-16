from lib import digits
from math import factorial

def chain(n):
	count = 0
	mem = set()
	while n not in mem:
		count += 1
		mem.add(n)
		n = sum(map(factorial, digits(n)))
	return count

def main(limit):
	# silly brute force
	return sum(chain(n) == 60 for n in range(limit))

print(main(10 ** 6)) # 402
