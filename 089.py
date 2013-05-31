from itertools import groupby
from sys import stdout

to = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
fr = {}
for k, v in to.items():
	fr[v] = k
denominations = sorted(list(fr.keys()), reverse=True)

def numeral2num(numeral):
	stack = []
	for t in map(to.get, numeral):
		while stack and stack[-1] < t:
			t -= stack.pop()
		stack.append(t)
	return sum(stack)

def numlist2numeral(numlist):
	return ''.join(map(fr.get, numlist))

def num2numeral(n):
	numeral = ''
	for k in denominations:
		while k <= n:
			numeral += fr[k]
			n -= k
	repl = (
		('DCCCC', 'CM'),
		('CCCC','CD'),
		('LXXXX','XC'),
		('XXXX','XL'),
		('VIIII', 'IX'),
		('IIII', 'IV')
	)
	for k, v in repl:
		numeral = numeral.replace(k, v)
	return numeral

def main(filename):
	saved = 0
	with open(filename) as f:
		for line in f:
			numeral = line.strip()
			print(numeral, end=", ")
			stdout.flush()
			num = numeral2num(numeral)
			print(num, end=", ")
			stdout.flush()
			numeral2 = num2numeral(num)
			print(numeral2)
			stdout.flush()
			saved += len(numeral) - len(numeral2)
	return saved

# I had to look up the solution method because I was getting incorrect answers.
# I still don't know what the problem is, my old solution would minimize too much (to 956).
# Is there a rule against IVIV being a valid way of saying 8?
if __name__ == '__main__':
	print(main("089.txt")) # 743

