def main(w, h):
	# trick: use dynamic programming
	w, h = w + 1, h + 1 # number of cells to number of vertices
	cell = [[0] * w for _ in range(h)]
	for i in range(w):
		cell[0][i] = 1
	for j in range(h):
		cell[j][0] = 1
	for d in range(1, min(w, h)):
		for j in range(d, h):
			for i in range(d, w):
				cell[j][i] = cell[j - 1][i] + cell[j][i - 1]
	return cell[h - 1][w - 1]

print(main(20, 20)) # 137846528820
