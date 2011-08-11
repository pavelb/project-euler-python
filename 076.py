def main(lim):
	# two or more components, 100 = 100 does not count
	cache = dict()
	def decompose(target, i = 1):
		if target == 0:
			return 1
		if target < 0:
			return 0
		key = '%s.%s' % (target, i)
		if key not in cache:
			cache[key] = sum(decompose(target - n, n) for n in range(i, target + 1))
		return cache[key]
	return decompose(lim) - 1

print(main(100))