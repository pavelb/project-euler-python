from lib import pythagoreanTriples, square
from collections import defaultdict

# x + y and x - y are square so their product is square
# hence x*x - y*y = a*a or a*a + y*y = x*x
# similarly b*b + z*z = x*x and c*c + z*z = y*y
# keep generating pythagorean triplets and stop once such a trio is found
# and it solves the original constraint.

def main():
    xs = defaultdict(set)
    for p, q, x in pythagoreanTriples():
        for r, s in xs[x]:
            for y, z in ((p, r), (r, p), (p, s), (s, p), (q, r), (r, q), (q, s), (s, q)):
                if y > z and square(y * y - z * z):
                    if all(square(n) for n in [x+y,x-y,x+z,x-z,y+z,y-z]):
                        return x + y + z
        xs[x].add((p, q))

if __name__ == '__main__':
	print(main())  # 1006193
