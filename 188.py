import sys
sys.setrecursionlimit(2048)
# only works if a^m % m = 1
def tetratemod(a, k, m): return 1 if k == 0 else pow(a, tetratemod(a, k - 1, m), m)
print(pow(1777, 10 ** 8, 10 ** 8))
print(tetratemod(1777, 1855, 10 ** 8))
