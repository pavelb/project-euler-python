<<<<<<< HEAD
from lib import charInd, triangular

def main(file):
	with open(file, 'r') as f:
		words = f.readline().replace('"', '').split(',')
	charSum = lambda word: sum(map(charInd, word))
	sums = map(charSum, words)
	return sum(map(triangular, sums))

print(main('042.txt')) # 162
=======
from lib import charInd, triangular

def main(file):
	with open(file, 'r') as f:
		words = f.readline().replace('"', '').split(',')
		return sum(triangular(sum(map(charInd, word))) for word in words)

print(main('042.txt')) # 162
>>>>>>> upstream/master
