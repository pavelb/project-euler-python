from itertools import count
from math import sqrt

def main(limit):
	i = 0
	for m in count(0):
		a = pow(9 - 4 * sqrt(5), 2 * m)
		b = pow(9 + 4 * sqrt(5), 2 * m)

		layer = [
			((-2 + sqrt(5)) * a + (-2 - sqrt(5)) * b - 1) / 5.0, \
			((-2 - sqrt(5)) * a + (-2 + sqrt(5)) * b - 1) / 5.0, \
			((+1 - sqrt(5)) * a + (+1 + sqrt(5)) * b - 2) / 10.0, \
			((-29 + 13 * sqrt(5)) * a + (-29 - 13 * sqrt(5)) * b - 2) / 10.0, \
			((11 - 5 * sqrt(5)) * a + (+11 + 5 * sqrt(5)) * b - 2) / 10.0, \
			((1 + sqrt(5)) * a + (+1 - sqrt(5)) * b - 2) / 10.0
		]

		for n in sorted(filter(lambda n: n > 0, layer)):
			i += 1
			if i == limit:
				return int(n)

print(main(15)) # 1120149658760
