# not finished
from heapq import heappush, heappop

def snm(n):
	if n <= 1: return 0
	if n % 2 == 0: return 1 + snm(n // 2)
	return 1 + snm(n - 1)

def binary_search(a, x, lo = 0, hi = None):
	if hi is None:
		hi = len(a)
	while lo < hi:
		mid = (lo + hi) // 2
		midval = a[mid]
		if midval < x:
			lo = mid + 1
		elif midval > x:
			hi = mid
		else:
			return mid
	return - 1

def sumProperDivisors(input, depth, lowest):
	#print(input, depth, lowest)
	if len(input) - 1 + depth >= lowest:
		return lowest
	n = -heappop(input)
	if n == 1:
		return depth
	depth += 1
	for a in range(1, n // 2 + 1):
		b = n - a
		#print(a, b)
		input2 = list(input)
		if binary_search(input2, -a) == -1:
			heappush(input2, -a)
		if binary_search(input2, -b) == -1:
			heappush(input2, -b)
		lowest = min(lowest, sumProperDivisors(input2, depth, lowest))
	return lowest

def main(n):
	return sumProperDivisors([-n], 0, snm(n))

print(main(200))
