from lib import ngonalNums
from itertools import dropwhile, takewhile

def ngonalNumsOfLen(n, digits):
	lbound = pow(10, digits - 1)
	ubound = 10 * lbound
	return list(takewhile(lambda n: n < ubound, dropwhile(lambda n: n < lbound, ngonalNums(n))))

tri, squ, pen, hex, hep, oct = range(6)
nums = [[], [], [], [], [], []]
nums[tri] = ngonalNumsOfLen(3, 4)
nums[squ] = ngonalNumsOfLen(4, 4)
nums[pen] = ngonalNumsOfLen(5, 4)
nums[hex] = ngonalNumsOfLen(6, 4)
nums[hep] = ngonalNumsOfLen(7, 4)
nums[oct] = ngonalNumsOfLen(8, 4)

def frontOf(n):
	return n // 100

def backOf(n):
	return n % 100

def get(tuple, req):
	if len(req) == 0:
		if frontOf(tuple[0]) == backOf(tuple[-1]):
			yield tuple
	else:
		for i in range(len(req)):
			newreq = req[:i] + req[i + 1:]
			for n in nums[req[i]]:
				if frontOf(n) == backOf(tuple[-1]):
					for rv in get(tuple + [n], newreq):
						yield rv

def main():
	return next(sum(tuple) for n in nums[tri] for tuple in get([n], [1, 2, 3, 4, 5]))

print(main()) # 28684
