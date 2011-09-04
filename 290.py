import random

def sumDigits(n):
	rv = 0
	while n:
		rv += n % 10
		n //= 10
	return rv

count = 0
for i in range(int(10 ** 3 / 9)):
	n = 9 * i
	n1 = n
	n2 = 137 * n
	a = sumDigits(n1)
	b = sumDigits(n2)
	if a > b:
		# print(n1, n2)
		count += 1
print(count)
