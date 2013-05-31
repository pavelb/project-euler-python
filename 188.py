import sys
sys.setrecursionlimit(2048)

# only works if a^m % m = 1
def tetratemod(a, k, m):
	return 1 if k == 0 else pow(a, tetratemod(a, k - 1, m), m)

def main(a, b, c):
	return tetratemod(b, c, 10 ** a)

if __name__ == '__main__':
	print(main(8, 1777, 1855)) # 95962097
