from lib import digits, pandigital

def cp(n):
	# concatenate products and check if pandigital
	rv = ''
	m = 0
	while len(rv) < 9:
		m += n
		rv += str(m)
	rv = int(rv)
	return rv if pandigital(rv) else - 1

def main():
	# brute force
	# we need the max value of the base integer
	# max pandigital number is 999999999 and min n is 2 so [i][2i] = 999999999
	# since |[i]| <= |[2i]| have [i][2i] = [9999][99999] giving i = 9999
	return max(map(cp, range(1, 9999)))

print(main()) # 932718654
