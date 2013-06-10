from lib import ngonalNums, pentagonal

def main():
	for Pa in ngonalNums(5):
		for Pb in ngonalNums(5):
			if Pb >= Pa:
				break
			if pentagonal(Pa + Pb) and pentagonal(Pa - Pb):
				return Pa - Pb

if __name__ == '__main__':
	print(main()) # 5482660
