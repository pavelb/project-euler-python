def readable(ascii):
	return ''.join(chr(a) for a in ascii)

def solveFor(encoded, start):
	for k in range(97, 122 + 1):
		e = encoded[:]
		good = True
		for i in range(start, len(e), 3):
			e[i] ^= k
			if e[i] < 32 or e[i] > 122:
				good = False
				break
		if good:
			yield k, e

def keys(encoded):
	for ak, a in solveFor(encoded, 0):
		for bk, b in solveFor(a, 1):
			for ck, c in solveFor(b, 2):
				yield [ak, bk, ck], chr(ak) + chr(bk) + chr(ck), readable(c)

def main():
	rv = []
	with open('059.txt') as f:
		data = f.read().split(',')
	encoded = list(map(int, data))
	for key, keyStr, text in keys(encoded):
		enc = encoded[:]
		for i in range(len(enc)):
			enc[i] ^= key[i % 3]
		rv.append('%s\n%s - %s' % (text, keyStr, sum(enc)))
	return '\n'.join(rv)

if __name__ == '__main__':
	print(main()) # 107359
