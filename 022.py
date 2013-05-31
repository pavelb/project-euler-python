from lib import charInd

def main(file):
	with open(file, 'r') as f:
		names = sorted(f.readline().replace('"', '').split(','))
		return sum((i + 1) * sum(map(charInd, name)) for i, name in enumerate(names))

if __name__ == '__main__':
	print(main('022.txt')) # 871198282
