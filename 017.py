def namer(n, over100 = False):
	names = [
		(1000000000, 'billion'),
		(1000000, 'million'),
		(1000, 'thousand'),
		(100, 'hundred')
	]
	
	names2 = [
		(90, 'ninety'),
		(80, 'eighty'),
		(70, 'seventy'),
		(60, 'sixty'),
		(50, 'fifty'),
		(40, 'forty'),
		(30, 'thirty'),
		(20, 'twenty'),
		(19, 'nineteen'),
		(18, 'eighteen'),
		(17, 'seventeen'),
		(16, 'sixteen'),
		(15, 'fifteen'),
		(14, 'fourteen'),
		(13, 'thirteen'),
		(12, 'twelve'),
		(11, 'eleven'),
		(10, 'ten'),
		(9, 'nine'),
		(8, 'eight'),
		(7, 'seven'),
		(6, 'six'),
		(5, 'five'),
		(4, 'four'),
		(3, 'three'),
		(2, 'two'),
		(1, 'one')
	]
	
	for k, label in names:
		if n >= k:
			return namer(n // k) + [label] + namer(n % k, True)
	
	prefix = ['and'] if over100 else []
	
	for k, label in names2:
		if n >= k:
			return prefix + [label] + namer(n % k, False)
	
	return []

def name(n):
	names = namer(n)
	return 'zero' if len(names) == 0 else ''.join(names)

def main(lim):
	return sum(len(name(n)) for n in range(1, lim + 1))

print(main(1000))