def pandigital(n):
    return len(n) == 9 and len(set(map(int, n)) ^ set(range(1, 10))) == 0

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
	# max pandigital number is 999999999 and min n is 2 so [i][2i] = 999999999
	# since |[i]| <= |[2i]| have [i][2i] = [9999][99999] giving i = 9999
	return max(cp(i) for i in range(1, 9999))

print p38()