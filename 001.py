def smk(k, n): # sum of multiples of k in [2, n)
	nd = (n - 1) // k
	return k * nd * (nd + 1) // 2

def main(n):
	return smk(3, n) + smk(5, n) - smk(3 * 5, n)

if __name__ == '__main__':
	print(main(1000)) # 233168
