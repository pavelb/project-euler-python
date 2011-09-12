<<<<<<< HEAD
from lib import ngonalNums, pentagonal, hexagonal

def main(limit):
	return next(n for n in ngonalNums(3) if n > limit and pentagonal(n) and hexagonal(n))

print(main(40755)) # 1533776805
=======
from lib import ngonalNums, pentagonal, hexagonal

def main(limit):
	return next(n for n in ngonalNums(3) if n > limit and pentagonal(n) and hexagonal(n))

print(main(40755)) # 1533776805
>>>>>>> upstream/master
