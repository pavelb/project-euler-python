from itertools import permutations, chain

def main(sides, lim):
	# trick: brute force the cycle then check if leftover numbers can fill the outer nodes
	nums = range(1, 2 * sides + 1)
	maximum = 0
	for inner in permutations(nums, sides):
		outer = [n for n in nums if n not in inner]
		innerSums = [sum(pair) for pair in zip(inner, inner[1:] + inner[0:])]
		target = max(innerSums) + min(outer)
		outerSums = [target - n for n in innerSums]
		if sorted(outerSums) == outer:
			_, indexMin = min((n, i) for i, n in enumerate(outerSums))
			indices = chain(range(indexMin, sides), range(indexMin))
			soln = ((outerSums[i], inner[i], inner[(i + 1) % sides]) for i in indices)
			n = ''.join(map(str, chain.from_iterable(soln)))
			if len(n) == lim:
				maximum = max(maximum, int(n))
	return maximum

print(main(5, 16)) # 6531031914842725
