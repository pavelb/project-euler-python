def main(k, blocks):
	fill = [0] * (blocks + 1)
	sums = [0] * (blocks + 1)
	fill[0] = 1
	sums[0] = 1
	for n in range(1, blocks + 1):
		fill[n] = sums[n - 1] - sums[n - k - 1]
		sums[n] = sums[n - 1] + fill[n]
	return fill[blocks]

print(main(4, 50)) # 100808458960497
