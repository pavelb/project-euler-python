# not finished

import random

def ndtst(digits, digitsum, first=True):
	if not (0 <= digitsum <= 9 * digits): return
	if digits == 1:
		yield digitsum
	else:
		m = 10 ** (digits - 1)
		for d in (range(1, 10) if first else range(10)):
			for n in ndtst(digits - 1, digitsum - d, False):
				yield d * m + n

def st(digitsum, digitlimit):
	for digits in range(1, digitlimit):
		for n in ndtst(digits, digitsum):
			yield n

def p290(digitlimit):
	for d in range(1, digitlimit):
		for n in st(9 * d, digitlimit):
			if n % 137 == 0:
				print(n // 1233)

p290(6)

def cmm(degree, r, m):
	kmin = 0
	kmax = (10 ** (degree + 1) - 1 - r) // m
	for k in range(kmin, kmax + 1):
		print("(general polynomial of degree %d evaluated at 10) = %d" % (degree, r + 137 * k))

#print(cmm(2, 0, 137))
