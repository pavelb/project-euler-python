def main(k, blocks):
	# I took my original solution and played with the code
	# turns out there is a nice equation for the running total
	rs = [0] * (blocks + 1)
	rs[0] = 1
	for n in range(1, k + 1):
		rs[n] = 2 * rs[n - 1]
	for n in range(k + 1, blocks + 1):
		rs[n] = 2 * rs[n - 1] - rs[n - (k + 1)]
	return rs[blocks] - rs[blocks - 1]

if __name__ == '__main__':
	print(main(4, 50)) # 100808458960497
