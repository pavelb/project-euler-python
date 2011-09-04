from math import floor

def f(x): return floor(2 ** (30.403243784 - x ** 2)) / 10 ** 9

def p197():
	n = -1
	last = 0
	while True:
		np = f(n)
		a = n + np
		if last == a: return a
		last = a
		n = np

print(p197())