from lib import ngonalNums, pentagonal, hexagonal

def main(limit):
	return next(n for n in ngonalNums(3) if n > limit and pentagonal(n) and hexagonal(n))

if __name__ == '__main__':
	print(main(40755)) # 1533776805
