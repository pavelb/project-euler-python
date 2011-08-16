from lib import ngonalNums

def main(limit):
	# trick: "merge" the sorted lists until a match is found
	gens = [ngonalNums(3), ngonalNums(5), ngonalNums(6)]
	nums = list(map(next, gens))
	while nums[0] <= limit or not all(n == nums[0] for n in nums):
		i, _ = min(enumerate(nums), key = lambda t: t[1])
		nums[i] = next(gens[i])
	return nums[0]

print(main(40755)) # 1533776805
