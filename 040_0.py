from lib import digits
from itertools import count

def main(indices):
	# brute force
	index = 0
	pos = 1
	rv = 1
	for n in count(1):
		d = list(digits(n))
		while indices[index] - pos < len(d):
			rv *= d[indices[index] - pos]
			index += 1
			if index == len(indices):
				return rv
		pos += len(d)
	return rv

print(main([1, 10, 100, 1000, 10000, 100000, 1000000])) # 210
