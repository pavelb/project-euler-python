from lib import CFRparts

def period(iterable):
	mem = set()
	for i, item in enumerate(iterable):
		if item in mem:
			return i - 1
		mem.add(item)
	return 0

def main(lim):
	return sum(period(CFRparts(n)) % 2 for n in range(2, lim + 1))

if __name__ == '__main__':
	print(main(10000)) # 1322
