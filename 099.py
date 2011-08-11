from math import log10

def main():
	nums = (map(int, i.split(',')) for i in open('099.txt').read().split('\n'))
	_, line = max((e * log10(b), i + 1) for i, (b, e) in enumerate(nums))
	return line

print(main())