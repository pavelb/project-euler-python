from lib import num
from itertools import permutations

def main(length):
	# generate all pandigital numbers and try inserting * and = everywhere
	def seq(length):
		nums = set(range(1, length + 1))
		for ansLen in range(1, length - 1):
			for ansDigits in permutations(nums, ansLen):
				ans = num(ansDigits)
				dgen = permutations(nums - set(ansDigits))
				igen = range(1, length - ansLen - 1)
				if any(num(d[:i]) * num(d[i:]) == ans for d in dgen for i in igen):
					yield ans
	return sum(seq(length))

if __name__ == '__main__':
	print(main(9)) # 45228
