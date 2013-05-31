from math import log10

def main(file):
	# trick: compare logs
	with open(file, 'r') as f:
		nums = [tuple(map(int, line.rstrip().split(','))) for line in f]

	def log(i):
		b, e = nums[i]
		return e * log10(b)

	return 1 + max(range(len(nums)), key=log)

if __name__ == '__main__':
	print(main('099.txt')) # 709
