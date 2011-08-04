def pandigital(n):
    digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
	return len(n) == 9 and len(set(map(int, n)) ^ digits) == 0

def cp(i):
	# concatenate products and check if pandigital
	concat = ''
	n = 1
	while len(concat) < 9:
		concat += str(i * n)
		n += 1
	return int(concat) if pandigital(concat) else -1

def p38():
	# lets do a dummy brute force
	# we need the max value of the base integer
	# max 9-digit pandigital number is 999999999 and smallest n is 2 so [i][2i] = 999999999
	# since |[i]| <= |[2i]| only option is [i][2i] = [9999][99999] giving i = 9999
	return max(cp(i) for i in range(1, 9999))

print(p38())
