# This is so terrible, it took about 5 minutes to get the answer

def reverse(n):
	rv = 0
	while n > 0:
		rv = rv * 10 + n % 10
		n /= 10
	return rv

def onlyOddDigits(n):
	while n > 0:
		if n % 2 == 0: return False
		n /= 10
	return True

def p145():
	count = 0
	n = 1000000000
	while n != 0:
		n -= 1
		if n % 10 == 0: continue
		if onlyOddDigits(n + reverse(n)):
			print(n)
			count += 1
	return count

print(p145())
