def timesc(c, iterable):
	return [c * i for i in iterable]

def plus(i1, i2):
	return [a + b for a, b in zip(i1, i2)]

def step(turns):
	poly = [1, 1]
	for n in range(2, turns + 1):
		poly = plus(poly + [0], [0] + timesc(n, poly))
	k = sum(divmod(turns, 2))
	return sum(poly[:k]), sum(poly)

def main(turns):
	n, d = step(turns)
	return d // n

if __name__ == '__main__':
	print(main(15)) # 2269
