from itertools import count, product
from lib import num

def main(exp):
	rv = 0
	for r in count(2):
		for d in product(range(10), repeat=r):
			if d[0] == 0:
				continue
			n = num(d)
			if (n - sum(d)) % exp: # assume exp is prime and use fermats theorem
				continue
			if n == sum(b ** exp for b in d):
				rv += n
		if 10 ** r > 9 ** exp * r: # if max rhs smaller than min lhs
			break
	return rv

if __name__ == '__main__':
	print(main(5)) # 443839
