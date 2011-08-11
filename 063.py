def main():
	# 10 ^ e has e + 1 digits, so max base is 9
	# 9 ^ 22 has 21 digits, so 21 is the max exp
	return sum(len(str(pow(b, e))) == e for e in range(1, 22) for b in range(1, 10))

print(main())