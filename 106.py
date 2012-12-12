from itertools import chain, combinations

# if we know a < b and c < d then clearly a + c < b + d so that if
# B = (a, b) and C = (c, d) we dont need to check these for equality


def main(n):
	arr = list(range(n))

	count = 0
	for r in range(2, len(arr) // 2 + 1):
		for B, C in combinations(combinations(arr, r), 2):
			if set(B) & set(C):
				continue
			# at this point we have two disjoint subsets of size r
			if any(a >= b for a, b in zip(B, C)):
				count += 1

	return count

print(main(12))  # 21384
