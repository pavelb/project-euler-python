<<<<<<< HEAD
def main(k, limit):
	mask = pow(10, k)
	rv = 0
	for n in range(1, limit + 1):
		rv = (rv + pow(n, n, mask)) % mask
	return rv

print(main(10, 1000)) # 9110846700
=======
def main(digits, limit):
	mask = pow(10, digits)
	rv = 0
	for n in range(1, limit + 1):
		rv = (rv + pow(n, n, mask)) % mask
	return rv

print(main(10, 1000)) # 9110846700
>>>>>>> upstream/master
