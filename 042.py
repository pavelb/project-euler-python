from lib import charInd, square

def triangular(n):
	return square(8 * n + 1)

def main(file):
	with open(file, 'r') as f:
		words = f.readline().replace('"', '').split(',')
		return sum(triangular(sum(map(charInd, word))) for word in words)

print(main('042.txt')) # 162
