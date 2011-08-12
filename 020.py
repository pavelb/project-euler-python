from lib import digits
from math import factorial

def main(n):
	return sum(digits(factorial(n)))

print(main(100)) # 648
