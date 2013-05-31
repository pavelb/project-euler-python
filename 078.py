from lib import partitionFnGen

def main(limit):
	return 1 + next(i for i, n in enumerate(partitionFnGen()) if n % limit == 0)

if __name__ == '__main__':
	print(main(1000000)) # 55374
