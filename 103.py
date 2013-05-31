from itertools import *


def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def candidates(start, n, limit):
	can = list(range(start, start + n))
	yield list(can)

	while True:
		for i in range(len(can) - 1, -1, -1):
			can[i] += 1

			for j in range(i + 1, len(can)):
				can[j] = can[j - 1] + 1

			if sum(can) <= limit:
				yield list(can)
				break

			if i == 0:
				return


def good(arr):
	arr = sorted(arr)

	# Step 1: Check "if B contains more elements than C then sum(B) > sum(C)
	# Do this by comparing the smallest n + 1 elements to the largest n elements
	#                      |----------- B -----------|        |------- C ------|

	for n in range(1, (len(arr) + 1) // 2):
		if sum(arr[:n + 1]) < sum(arr[-n:]):
			return False

	# Step 2: Check "sum(B) != sum(C)"

	sums = sorted(map(sum, powerset(arr)))
	for i in range(1, len(sums)):
		if sums[i - 1] == sums[i]:
			return False

	return True


def solve(n):
	if n == 1:
		return [1]

	smallSoln = solve(n - 1)
	mid = smallSoln[len(smallSoln) // 2]
	candidateSoln = [mid] + list(map(lambda n: n + mid, smallSoln))
	limit = sum(candidateSoln)

	return min(filter(good, candidates(mid, n, limit)), key=sum)


def main(n):
	return ''.join(map(str, solve(n)))


if __name__ == '__main__':
	print(main(7))  # 20313839404245
