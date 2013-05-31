def main(nums, target, i = 0):
	if target == 0:
		return 1
	if i >= len(nums):
		return 0
	return sum(main(nums, target - n, i + 1) for n in range(0, target + 1, nums[i]))

if __name__ == '__main__':
	print(main([1, 2, 5, 10, 20, 50, 100, 200], 200)) # 73682
