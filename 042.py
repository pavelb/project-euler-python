from lib import charInd, triangular

def main(file):
	with open(file, 'r') as f:
		words = f.readline().replace('"', '').split(',')
	charSum = lambda word: sum(map(charInd, word))
	sums = map(charSum, words)
	return sum(map(triangular, sums))

if __name__ == '__main__':
	print(main('042.txt')) # 162
