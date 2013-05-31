from lib import choose

def main(limit, target):
	return sum(choose(n, k) > target for n in range(1, limit + 1) for k in range(1, n))

if __name__ == '__main__':
	print(main(100, 1000000)) # 4075
