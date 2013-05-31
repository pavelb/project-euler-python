from lib import num
from itertools import permutations, combinations

def countConsecutive(iterable):
	for i, v in enumerate(iterable):
		if i + 1 != v:
			return i
	return 0

def operationsOn(a, b):
	yield a + b
	yield a - b
	yield a * b
	if b != 0:
		yield float(a) / b

def equationsOn(terms):
	if len(terms) == 1:
		yield terms[0]
	else:
		for i in range(len(terms) - 1):
			for val in operationsOn(terms[i], terms[i + 1]):
				for ans in equationsOn(terms[:i] + [val] + terms[i + 2:]):
					yield ans

def countStreak(terms):
	rv = []
	for termPerm in permutations(terms):
		for ans in equationsOn(list(termPerm)):
			if ans > 0 and ans == int(ans):
				rv.append(ans)
	return countConsecutive(sorted(set(rv)))

def main():
	return num(max(combinations(range(10), 4), key=countStreak))

if __name__ == '__main__':
	print(main()) # 1258
