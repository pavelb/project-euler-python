from math import factorial

def main(n):
	return sum(map(int, str(factorial(n))))

print(main(100))