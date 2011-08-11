def main(file):
	offset = ord('A') - 1
	with open(file, 'r') as f:
		names = sorted(f.readline().replace('"', '').split(','))
		return sum((i + 1) * sum(ord(c) - offset for c in name) for i, name in enumerate(names))

print(main('022.txt'))