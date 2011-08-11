def main(nums, target):
	if target == 0:
		return 1
	if target < 0 or len(nums) == 0:
		return 0
	rest = nums[1:]
	return sum(main(rest, target - n) for n in range(0, target + 1, nums[0]))

print(main([1, 2, 5, 10, 20, 50, 100, 200], 200))