def main(n):
	# trick: dividing out factors in increasing order guarantees their primeness
	k = 2
	rv = None
	while k <= n:
		if n % k == 0:
			n //= k
			rv = k
		k += 1
	return rv

print(main(600851475143))