from lib import convergents

def main(limit):
	# Case 1: a, a, a + 1
	#	for integer area a must be odd, a = 2 * k1 + 1
	#	this leads to:
	#		p1 = 3*a + 1 = 6*k1 + 4
	#		(3*k1+1)^2 - 3*s^2 = 1 for some integer s
	# Case 2: a, a, a - 1
	#	for integer area a must be odd, a = 2 * k2 + 1
	#	this leads to:
	#		p2 = 3*a - 1 = 6*k2 + 2
	#		(3*k2+2)^2 - 3*s^2 = 1 for some integer s

	rv = 0
	# get all t and s such that t^2 - 3*s^2 = 1
	for x, y in convergents(3):
		if x >= 4 and x * x - 3 * y * y == 1:
			t = x
			p1 = 2 * (t - 1) + 4
			p2 = 2 * (t - 2) + 2
			if p1 > limit and p2 > limit:
				return rv
			if p1 <= limit and (t - 1) % 3 == 0:
				rv += p1
			if p2 <= limit and (t - 2) % 3 == 0:
				rv += p2

print(main(10 ** 9)) # 518408346
