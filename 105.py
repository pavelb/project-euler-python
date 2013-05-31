from itertools import chain, combinations


def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def good(arr):
	line = sorted(powerset(arr), key=sum)

	for i in range(1, len(line)):
		last = line[i - 1]
		tuple = line[i]

		if len(last) > len(tuple):
			return False

		if sum(last) == sum(tuple):
			return False

	return True


def solve(file):
	for line in file:
		arr = list(map(int, line.strip().split(',')))
		if good(arr):
			yield arr


def main(filename):
	with open(filename, 'r') as file:
		return sum(map(sum, solve(file)))


if __name__ == '__main__':
	print(main('105.txt'))  # 73702
