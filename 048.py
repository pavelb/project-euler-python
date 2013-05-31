def main(k, limit):
	mask = pow(10, k)
	rv = 0
	for n in range(1, limit + 1):
		rv = (rv + pow(n, n, mask)) % mask
	return rv

if __name__ == '__main__':
	print(main(10, 1000)) # 9110846700
