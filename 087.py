from lib import Primes

primes = Primes()

def main(limit):
	mem = [False] * limit
	for pa in primes.gen():
		sq = pa * pa
		if sq > limit:
			break
		for pb in primes.gen():
			cu = pb * pb * pb
			if sq + cu > limit:
				break
			for pc in primes.gen():
				fo = pc * pc * pc * pc
				tot = sq + cu + fo
				if tot > limit:
					break
				mem[tot] = True
	return sum(mem)

if __name__ == '__main__':
	print(main(50000000)) # 1097343
