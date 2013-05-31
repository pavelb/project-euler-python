from itertools import count

def good(n, exp):
	on = n
	m = 0
	while n > 0 and m <= on:
		m += pow(n % 10, exp)
		n //= 10
	return m == on

def main(exp):
	limit = next(n for n in count(1) if pow(10, n) > pow(9, exp) * n)
	return sum(n for n in range(2, pow(10, limit)) if good(n, exp))

if __name__ == '__main__':
	print(main(5)) # 443839
