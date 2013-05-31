# worked for euler but is not correct.
# must consider remaining cards as tie breaker if tuples match

number_map = dict(zip(list("23456789TJQKA"), range(1, 14)))
suit_map = dict(zip(list("CHSD"), range(4)))

def flush(hand):
	return len(set(suit for _, suit in hand)) == 1

def royal_flush(hand):
	return flush(hand) and has_number(hand, number_map["T"]) and has_number(hand, number_map["A"])

def straight(hand):
	def check(number):
		a, b, c, d, e = number
		return a + 1 == b and b + 1 == c and c + 1 == d and d + 1 == e
	number = [number for number, _ in hand]
	rv = check(number)
	if number_map["A"] in number:
		number.remove(number_map["A"])
		number.append(0)
		number.sort()
		rv = rv or check(number)
	return rv

def fix(hand):
	return sorted([(number_map[n], suit_map[s]) for n, s in hand])

def has_number(hand, number):
	return number in (number for number, _ in hand)

def count_numbers(hand):
	count = dict()
	for number, _ in hand:
		if number in count:
			count[number] += 1
		else:
			count[number] = 1
	return list(count.values())

def four(hand):
	return 4 in count_numbers(hand)

def full_house(hand):
	count = count_numbers(hand)
	return 2 in count and 3 in count

def three(hand):
	return 3 in count_numbers(hand)

def two_pair(hand):
	count = count_numbers(hand)
	if 2 in count:
		count.remove(2)
	else:
		return False
	return 2 in count

def pair(hand):
	return 2 in count_numbers(hand)

def highest(hand):
	return max(number for number, _ in hand)

def get(hand, n):
	count = dict()
	for number, _ in hand:
		if number in count:
			count[number] += 1
		else:
			count[number] = 1
	return [(k, 0) for k, v in count.items() if v == n]

def rank(hand):
	hand = fix(hand)
	if straight(hand) and flush(hand):
		return highest(hand) + 14 * 8
	if four(hand):
		return highest(get(hand, 2)) + 14 * 7
	if full_house(hand):
		return highest(hand) + 14 * 6
	if flush(hand):
		return highest(hand) + 14 * 5
	if straight(hand):
		return highest(hand) + 14 * 4
	if three(hand):
		return highest(get(hand, 3)) + 14 * 3
	if two_pair(hand):
		return highest(get(hand, 2)) + 14 * 2
	if pair(hand):
		return highest(get(hand, 2)) + 14 * 1
	return highest(hand)

def main(filename):
	count = 0
	with open(filename, 'r') as f:
		for line in f:
			a, b, c, d, e, f, g, h, i, j = line.strip().split(' ')
			if rank([a, b, c, d, e]) > rank([f, g, h, i, j]):
				count += 1
	return count

if __name__ == '__main__':
	print(main('054.txt')) # 376
