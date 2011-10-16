# not finished

def grow(order):
	if order == 0: return 0
	if order == 1: return 1
	if order == 2: return 2
	return polyomino(order - 2)

def growDir(xoffset, yoffset, order, com, hist):
	x, y = hist[-1]
	x += xoffset
	y += yoffset
	m = [x, y]
	return [] if m in hist else polyomino(order - 1, com + x, hist + [m])

def left(p): x, y = p; return [x - 1, y]
def up(p): x, y = p; return [x, y + 1]
def right(p): x, y = p; return [x + 1, y]

def balanced(sculpture): return sum(x for x, _ in sculpture) == 0

def polyomino(order):
	sculptures = [[[0, 0]]]
	for _ in range(order):
		tmpsculptures = []
		for sculpture in sculptures:
			for block in sculpture:
				p = left(block)
				if p not in sculpture: tmpsculptures.append(sculpture + [p])
				p = up(block)
				if p not in sculpture: tmpsculptures.append(sculpture + [p])
				p = right(block)
				if p not in sculpture: tmpsculptures.append(sculpture + [p])
		sculptures = tmpsculptures

	for sculpture in sculptures: sculpture.sort()
	sculptures = sorted(sculptures)

	last = None
	for sculpture in sculptures:
		if sculpture != last and balanced(sculpture):
			yield sculpture
		last = sculpture

count = 0
for g in grow(6):
	count += 1
	print(g)
print(count)
