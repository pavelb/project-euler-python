from decimal import Decimal, getcontext, ROUND_UP

getcontext().prec = 14

def s(n, r):
	r = Decimal(str(r))
	n = Decimal(str(n))
	return 3 * (299 - 300 * r + (n - 299) * pow(r, n) - (n - 300) * pow(r, n + 1)) / pow(1 - r, 2)

def ltpe(dec1, dec2):
	places = Decimal(str(10 ** 14))
	a = int(dec1 * places)
	b = int(dec2 * places)
	return a == b

def main():
	left = Decimal(str(299.0 / 300.0 + 2.0 / 10 ** 2))
	right = Decimal(str(1 - 1.0 / 10 ** 6))
	last = left
	target = Decimal(str(-6 * 10 ** 11))

	while True:
		# invariants:
		#	s(5000, left) < target
		#	s(5000, right) > target
		center = (left + right) / 2
		t = s(5000, (left + right) / 2)
		# print(t, center)
		if ltpe(center, last): break
		elif t > target: right = center
		else: left = center
		last = center

	return center.quantize(Decimal('.000000000001'), rounding = ROUND_UP)

if __name__ == '__main__':
	print(main()) # 1.002322108633
