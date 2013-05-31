from lib import digits
from itertools import count

def increasing(d):
	return all(d[i] <= d[i + 1] for i in range(len(d) - 1))

def decreasing(d):
	return all(d[i] >= d[i + 1] for i in range(len(d) - 1))

def bouncy(n):
	d = digits(n)
	return not increasing(d) and not decreasing(d)

def main(target):
	b = 0
	for n in count(100):
		b += bouncy(n)
		if b > target * n:
			return n - 1

if __name__ == '__main__':
	print(main(0.99)) # 1587000
