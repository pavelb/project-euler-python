def cached(fn):
	cache = dict()
	def new(d, s = 0):
		key = d << 3 | s
		if key not in cache: cache[key] = fn(d, s)
		return cache[key]
	return new

transition = [[0, 1, 2], [1, 3], [0, 1, 4], [1, 5], [0, 1], [1]]

@cached
def main(depth, state = 0):
	if depth == 0: return 1
	depth -= 1
	return sum(main(depth, s) for s in transition[state])

if __name__ == '__main__':
	print(main(30)) # 1918080160
