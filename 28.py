def main(n):
	# trick: magic
	h = n // 2
	return 1 + 2 * h * (8 * h * h + 15 * h + 13) // 3

print(main(1001))