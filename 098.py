from lib import numLen, digits, num
from itertools import count, combinations

def swaps(word1, word2): # return the swaps required to turn word1 into word2
	temp = list(word1)
	for i, c in enumerate(word2):
		j = temp.index(c, i)
		if i != j:
			temp[j] = temp[i]
			yield i, j

def apply(word, swaps):
	word = list(word)
	for i, j in swaps:
		word[i], word[j] = word[j], word[i]
	return word

def main(file):
	# trick: for every anagram (word1, word2) calculate the character swaps
	# required to turn word2 into word1 then perform those swaps on a square
	# number of the same length as word1 and see if the resulting number is
	# a square. Only caveat is that the eligible square numbers must have
	# at most one of each digit

	with open(file, 'r') as f:
		words = f.read().replace('"', '').split(',')

	# group the words into lists of anagrams
	anagrams = dict()
	for word in words:
		anagrams.setdefault(''.join(sorted(word)), []).append(word)

	# group the anagram lists by the length of the word
	anagramsByLen = dict()
	for k, v in anagrams.items():
		if len(v) > 1:
			anagramsByLen.setdefault(len(k), []).append(v)

	# create eligible squares and group them by length
	squaresByLen = dict()
	for n in count(4):
		sq = n * n
		key = numLen(sq)
		if key not in anagramsByLen:
			break
		if key == len(set(digits(sq))): # no repeated digits
			squaresByLen.setdefault(key, []).append(sq)

	def results():
		for k in squaresByLen:
			squares = squaresByLen[k]
			for words in anagramsByLen[k]:
				for word1, word2 in combinations(words, 2):
					sw = list(swaps(word1, word2))
					for sq in squares:
						n = num(apply(digits(sq), sw))
						if n in squares:
							yield max(n, sq)

	return max(results())

print(main('098.txt')) # 18769
