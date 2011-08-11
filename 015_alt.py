def cached(fn):
	cache = dict()
	def new(w, h):
		key = str(h) + '.' + str(w)
		if key in cache: return cache[key]
		key = str(w) + '.' + str(h)
		if not key in cache: cache[key] = fn(w, h)
		return cache[key]
	return new

@cached
def main(w, h):
	return 1 if w == 0 or h == 0 else main(w - 1, h) + main(w, h - 1)

print(main(20, 20))