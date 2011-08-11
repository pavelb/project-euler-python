def palindrome(n):
	return str(n) == str(n)[::-1]

def seq(n, lim=54):
	for _ in range(lim):
		n += int(str(n)[::-1])
		yield n

def lycharel(n):
	return not any(map(palindrome, seq(n)))

def main(lim):
	return sum(map(lycharel, range(1, lim)))

print(main(10000))