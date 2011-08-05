def main(a, b):
	terms = set([])
	for i in range(2, a + 1):
		for j in range(2, b + 1):
			terms.add(pow(i, j))
	return len(terms)

print(main(100, 100))