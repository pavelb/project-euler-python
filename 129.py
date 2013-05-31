from itertools import count

def A(n):
	if n % 2 == 0 or n % 5 == 0: return 0
	for k in count(1):
		# if R(k) = (10^k - 1)/9 == 0 (mod n)
		if pow(10, k, 9 * n) == 1:
			return k

def main(limit):
	for n in count(limit):
		if A(n) > limit:
			return n

if __name__ == '__main__':
	print(main(10 ** 6)) # 1000023
