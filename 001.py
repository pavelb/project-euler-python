def smk(k, n): # sum of multiples of k in [2, n)
	nd = (n - 1) // k
	return k * nd * (nd + 1) // 2

def main(primeCount):
	return smk(3, primeCount) + smk(5, primeCount) - smk(3 * 5, primeCount)

if __name__ == '__main__':
	print(main(1000)) # 233168
