from lib import fibonacci

def main(limit):
	return next(n for n, f in enumerate(fibonacci()) if len(str(f)) >= limit)

print(main(1000)) # 4782
