from lib import digits
from itertools import count

def main(indices):
	index = 0
	pos = 1
	rv = 1
	for n in count(1):
		d = digits(n)
		while indices[index] - pos < len(d):
			rv *= d[indices[index] - pos]
			index += 1
			if index == len(indices):
				return rv
		pos += len(d)
	return rv

if __name__ == '__main__':
	print(main([1, 10, 100, 1000, 10000, 100000, 1000000])) # 210
