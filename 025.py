from lib import fibonacci, numLen

def main(limit):
	return next(n for n, f in enumerate(fibonacci()) if numLen(f) >= limit)

print(main(1000)) # 4782
