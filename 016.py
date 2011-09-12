from lib import digits

def main(n):
<<<<<<< HEAD
	return sum(digits(pow(2, n)))

print(main(1000)) # 1366
=======
	return sum(digits(n))

print(main(pow(2, 1000))) # 1366
>>>>>>> upstream/master
