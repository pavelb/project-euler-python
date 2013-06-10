from lib import ngonalNums, takeLen

def ngonalNumsOfLen(n, k):
	return list(takeLen(k, ngonalNums(n)))

tri, squ, pen, hex, hep, oct = range(6)
nums = [[], [], [], [], [], []]
nums[tri] = ngonalNumsOfLen(3, 4)
nums[squ] = ngonalNumsOfLen(4, 4)
nums[pen] = ngonalNumsOfLen(5, 4)
nums[hex] = ngonalNumsOfLen(6, 4)
nums[hep] = ngonalNumsOfLen(7, 4)
nums[oct] = ngonalNumsOfLen(8, 4)

def front(n):
	return n // 100

def back(n):
	return n % 100

def get(tuple, req):
	if len(req) == 0:
		if front(tuple[0]) == back(tuple[-1]):
			yield tuple
	else:
		for i in range(len(req)):
			newreq = req[:i] + req[i + 1:]
			for n in nums[req[i]]:
				if front(n) == back(tuple[-1]):
					yield from get(tuple + [n], newreq)

def main():
	return next(sum(tuple) for n in nums[tri] for tuple in get([n], [1, 2, 3, 4, 5]))

if __name__ == '__main__':
	print(main()) # 28684
