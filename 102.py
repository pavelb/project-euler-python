def hit(ax, ay, bx, by): # does the ray (t, 0) intersect line segment AB (not counting the points (0, 0), A, and B)
	return (ay > 0) != (by > 0) and (ay > by) == (ay * bx > by * ax)

def inside(ax, ay, bx, by, cx, cy): # is (0, 0) inside triangle ABC
	return (hit(ax, ay, bx, by) + hit(bx, by, cx, cy) + hit(cx, cy, ax, ay)) == 1

def main(file):
	# trick: consider an arbitrary ray. If the ray starts inside a triangle it
	# will intersect exactly 1 side. If the ray starts outside the triangle it
	# will intersect 0 or 2 sides.
	with open(file, 'r') as f:
		triangles = [tuple(map(int, line.rstrip().split(','))) for line in f]
	return sum(inside(*t) for t in triangles)

print(main('102.txt')) # 228
