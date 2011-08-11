from itertools import count

def main(lim):
	record = dict()
	d = 1
	for n in (n * n * n for n in count(1)):
		key = ''.join(sorted(str(n)))
		if len(key) > d:
			d = len(key)
			rv = None
			for tuple in record.values():
				if len(tuple) == lim:
					rv = min(rv, tuple[0]) if rv else tuple[0]
			if rv:
				return rv
			record.clear()
		if key in record:
			record[key].append(n)
		else:
			record[key] = [n]

print(main(5))