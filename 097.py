def main(a, b, k):
	mask = pow(10, k)
	return (a * pow(2, b, mask) + 1) % mask

if __name__ == '__main__':
	print(main(28433, 7830457, 10)) # 8739992577
