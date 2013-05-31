from lib import pythagoreanTriples
from math import sqrt

def countSolns(p, q): # p < q leads to simplification of first case
	yield q, p // 2 # q = a, p = b + c
	yield p, max(0, q // 2 - (q - p) + 1) # p = a, and q = b + c

def main(limit):
	# unwrap the box and draw straight lines from S to F
	# we see that the path is a hypotenuse
	# to get integer paths use pythagorean triples
	mem = [0] * 4
	for p, q, r in pythagoreanTriples(): # we let p, q = a, b + c or q, p = a, b + c
		for maxSide, solns in countSolns(p, q):
			if maxSide >= len(mem): # double the length of the list
				mem.extend([mem[-1]] * len(mem))
			for m in range(maxSide, len(mem)): # count this M toward larger Ms
				mem[m] += solns
		# p + q + r = p + q + sqrt(p * p + q * q) < 3*M + sqrt(5) * M
		M = int((p + q + r) / (3 + sqrt(5))) # Ms smaller or equal to this are fixed, ie no new solutions possible
		if mem[M] > limit:
			# Once we find a fixed M over the limit we should see if there is one smaller
			# I have a hunch that the one we found is the smallest but I can't prove it
			M = 1 + next(m for m in reversed(range(M)) if mem[m] <= limit) # smallest M that passes the limit
			return M

if __name__ == '__main__':
	print(main(10 ** 6)) # 1818
