def smk(k, n): # sum multiples of k that are in [2, n)
	nd = (n - 1) // k
	return k * nd * (nd + 1) // 2

def main(n):
	return smk(3, n) + smk(5, n) - smk(3 * 5, n)

print(main(1000))