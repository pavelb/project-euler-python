def main(nums, target):
	if target == 0:
		return 1
	if target < 0 or len(nums) == 0:
		return 0
	n = nums[0]
	nums = nums[1:]
	return sum(main(nums, target - i * n) for i in range(target // n + 1))

print(main([1, 2, 5, 10, 20, 50, 100, 200], 200))