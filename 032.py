from lib import num
from itertools import permutations, combinations, chain, product

def subsets(nums, sizes):
	for a in chain.from_iterable(combinations(nums, r) for r in sizes):
		a = set(a)
		yield a, nums - a


def genNums(digits):
	return map(num, permutations(digits))


def main(length):
	good = set()
	nums = set(range(1, length + 1))
	for restDigits, answerDigits in subsets(nums, range(2, len(nums))):
		answers = set(genNums(answerDigits))
		for leftDigits, rightDigits in subsets(restDigits, range(1, len(restDigits) // 2 + 1)):
			for a, b in product(genNums(leftDigits), genNums(rightDigits)):
				if a * b in answers:
					good.add(a * b)
	return sum(good)

if __name__ == '__main__':
	print(main(9)) # 45228
