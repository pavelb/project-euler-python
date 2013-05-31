def main(k, blocks):
	fill = [0] * (blocks + 1)
	sums = [0] * (blocks + 1)
	fill[0] = 1
	sums[0] = 1
	for n in range(1, blocks + 1):
		fill[n] = sums[n - 1] - sums[n - k - 1] # this may go negative, in which case it subtracts zeroes off the end
		sums[n] = sums[n - 1] + fill[n]
	return fill[blocks]

if __name__ == '__main__':
	print(main(4, 50)) # 100808458960497
