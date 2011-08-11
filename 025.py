def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

def main(limit):
	return next(n for n, f in enumerate(fibonacci()) if len(str(f)) >= limit)

print(main(1000))