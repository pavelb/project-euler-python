from lib import convergents

def main(limit):
	# B*(B-1)/T/(T-1) = 1/2		=>		2*(2*B-1)^2 - (2*T-1)^2 = 1
	# the solutions are the odd convergents of the Pell equation y^2 - 2*x^2 = -1
	for x, y in convergents(2):
		if x % 2 == 1 and y % 2 == 1 and x * x - 2 * y * y == -1:
			blue = (y + 1) // 2
			total = (x + 1) // 2
			if total > limit:
				return blue

print(main(10 ** 12)) # 756872327473
