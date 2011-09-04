def countInc(digits):
	# this is insane, it turns out the numbers are figurate
	# http://en.wikipedia.org/wiki/Figurate_number
	count = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(1, 10):
		count[i] = count[i - 1] * (digits - 1 + i) // i
	return sum(count)

def countDec(digits):
	return sum(map(countInc, range(digits + 1))) - digits # account for zeroes

def countIncAndDec(digits):
	return 1 + 9 * digits

def countNotBouncy(digits):
	return countInc(digits) + countDec(digits) - countIncAndDec(digits) - 1

def main(k):
	return countNotBouncy(k)

print(main(100)) # 51161058134250
