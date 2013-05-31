from itertools import count

def main(lim):
	record = dict()
	d = 1
	for i in count(1):
		n = i * i * i
		key = ''.join(sorted(str(n)))
		if len(key) > d: # length increased, check shorter nums
			d = len(key)
			good = lambda t: len(t) == lim
			goodNums = list(filter(good, record.values()))
			if goodNums:
				return min(min(goodNums))
			record.clear()
		record.setdefault(key, []).append(n)

if __name__ == '__main__':
	print(main(5)) # 127035954683
