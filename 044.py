from lib import ngonalNums, pentagonal
from itertools import takewhile

def main():
	for Pa in ngonalNums(5):
		for Pb in takewhile(lambda n: n < Pa, ngonalNums(5)):
			if pentagonal(Pa + Pb) and pentagonal(Pa - Pb):
				return Pa - Pb

if __name__ == '__main__':
	print(main()) # 5482660
