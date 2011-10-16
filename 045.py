from lib import ngonalNums, same

def main(limit):
	# trick: "merge" the sorted lists until a match is found
	gens = (ngonalNums(3), ngonalNums(5), ngonalNums(6))
	nums = list(map(next, gens))
	while nums[0] <= limit or not same(nums):
		i = min(range(3), key=lambda i: nums[i])
		nums[i] = next(gens[i])
	return nums[0]

print(main(40755)) # 1533776805
