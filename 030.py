from lib import digits
from itertools import count

def main(exp):
	limit = next(n for n in count(1) if pow(10, n) > pow(9, exp) * n)
	return sum(n for n in range(2, pow(10, limit)) if n == sum(pow(d, exp) for d in digits(n)))

print(main(5)) # 443839
