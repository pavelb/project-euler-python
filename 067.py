def main(file):
	# trick: bubble up the max values, summing along the way
	with open(file, 'r') as f:
		table = [list(map(int, line.strip().split(' '))) for line in f]
	gen = reversed(table)
	last = next(gen)
	for row in gen:
		for i, n in enumerate(row):
			row[i] = n + max(last[i], last[i + 1])
		last = row
	return table[0][0]

if __name__ == '__main__':
	print(main('067.txt')) # 7273
