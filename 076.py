from lib import partitionFn

def main(target):
	# two or more components, 100 = 100 does not count
	return partitionFn(target) - 1

print(main(100)) # 190569291
