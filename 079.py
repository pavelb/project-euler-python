def main(file):
	items = set()
	rules = set() # (a, b) means require pos(a) < pos(b)

	with open(file, 'r') as f:
		for line in f:
			a, b, c = line[:3]
			items.add(a)
			items.add(b)
			items.add(c)
			rules.add((a, b))
			rules.add((b, c))

	rv = ''

	while len(rules) > 0:
		first = set(a for a, _ in rules) - set(b for _, b in rules)
		rv += ''.join(first)
		items -= first
		rules = [(a, b) for a, b in rules if a not in first]

	return rv + ''.join(items)

print(main('079.txt')) # 73162890
