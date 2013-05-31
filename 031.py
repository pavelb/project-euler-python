def main(nums, target):
	mem = [[0] * len(nums) for _ in range(target + 1)]
	for n in range(target + 1):
		if n % nums[-1] == 0:
			mem[n][-1] = 1

	for i in range(len(nums) - 2, -1, -1):
		for n in range(target + 1):
			mem[n][i] = sum(mem[n - m][i + 1] for m in range(0, n + 1, nums[i]))

	return mem[target][0]

if __name__ == '__main__':
	print(main([1, 2, 5, 10, 20, 50, 100, 200], 200)) # 73682
