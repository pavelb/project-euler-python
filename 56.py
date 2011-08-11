def sumDigits(n):
	return sum(map(int, str(n)))

def main(lim):
	return max(sumDigits(pow(a, b)) for a in range(lim) for b in range(lim))

print(main(100))