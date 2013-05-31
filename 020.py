from lib import digits
from math import factorial

def main(n):
	return sum(digits(factorial(n)))

if __name__ == '__main__':
	print(main(100)) # 648
