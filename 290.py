from collections import defaultdict

# Let n be any 3 digit number and suppose we prepend digit d. We get
# n' = d*1000 + n. The sum of digits of n' is clearly the sum of digits of n
# plus d. Consider the sum of digits of 137*n' = 137*d*1000 + 137*n.
# Notice that the last three digits of this product must be the same as the last
# three digits of 137*n, which is a smaller problem. The trick is to process
# numbers in order of increasing length and storing enough information to
# be able to (a) check that the given property is satisfied and (b) easily make
# longer numbers.

N = 137

def prepend(digit, state):
	carry, sumDigitsDelta = state
	carry, digitN = divmod(N * digit + carry, 10)
	return carry, sumDigitsDelta + digit - digitN

def isGood(state):
	while state[0] > 0:
		state = prepend(0, state)
	return state[1] == 0

def main(digits):
	states = defaultdict(int)
	states[0, 0] = 1
	numGoodStates = 1

	for _ in range(digits):
		newStates = defaultdict(int)
		for state, count in states.items():
			for digit in range(10):
				newState = prepend(digit, state)
				newStates[newState] += count
				if digit > 0 and isGood(newState):
					numGoodStates += count
		states = newStates

	return numGoodStates

if __name__ == '__main__':
	print(main(18))  # 20444710234716473
