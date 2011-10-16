def cached(fn):
	cache = dict()
	def new(depth, n1 = 0, n2 = 0):
		key = depth << 8 | n1 << 4 | n2
		if key not in cache: cache[key] = fn(depth, n1, n2)
		return cache[key]
	return new

@cached
def gen(depth, n1 = 0, n2 = 0):
	return 1 if depth == 0 else sum(gen(depth - 1, n2, n3) for n3 in range(10 - n1 - n2))

def main(depth):
	return gen(depth) - gen(depth - 1)

print(main(20)) # 378158756814587
