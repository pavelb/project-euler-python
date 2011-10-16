def roll(sides, rolls):
	rv = [0]
	for _ in range(rolls):
		rv = [t + n for n in range(1, sides + 1) for t in rv]
	return group(rv)

def group(iterable):
	rv = dict()
	for i in iterable:
		if i in rv: rv[i] += 1
		else: rv[i] = 1
	return rv

def main(a, b, c, d):
	p1rolls = roll(a, b)
	p2rolls = roll(c, d)
	wins = 0
	for p1roll, p1count in p1rolls.items():
		for p2roll, p2count in p2rolls.items():
			if p1roll > p2roll:
				wins += p1count * p2count
	return round(float(wins) / a ** b / c ** d, 7)

print(main(4, 9, 6, 6)) # 0.5731441
