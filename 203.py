from lib import Primes, multiply
from itertools import takewhile

primes = Primes()

def addFactors(factors, ifactors):
	rv = factors[:]
	for fb, fe in ifactors:
		found = False
		for i, [b, e] in enumerate(rv):
			if b == fb:
				rv[i] = [b, e + fe]
				found = True
				break
		if not found:
			rv.append([fb, fe])
	return rv

def subtractFactors(factors, ifactors):
	rv = factors[:]
	for fb, fe in ifactors:
		found = False
		for i, [b, e] in enumerate(rv):
			if b == fb:
				if e == fe:
					del rv[i]
				else:
					rv[i] = [b, e - fe]
				found = True
				break
		if not found:
			rv.append([fb, -fe])
	return rv

def getNumber(factors):
	return multiply(b ** e for b, e in factors)

def factorOfFactorial(n):
	rv = []
	for i in range(2, n + 1):
		rv = addFactors(rv, primes.factors(i))
	return rv

def factorsOfChoose(n, k):
	return subtractFactors(subtractFactors(factorOfFactorial(n), factorOfFactorial(n - k)), factorOfFactorial(k))

def squareFree(factors):
	return all(c == 1 for _, c in factors)

def getKey(factors):
	return ",".join(str(f) + "." + str(c) for f, c in factors)

def main(rows):
	rv = 0
	hist = dict()
	for n in range(rows):
		for k in range(n // 2 + 1):
			num = factorsOfChoose(n, k)
			key = getKey(num)
			if key in hist: continue
			hist[key] = True
			if squareFree(num): rv += getNumber(num)
	return rv

print(main(51)) # 34029210557338
