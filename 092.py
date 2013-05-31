from lib import digits

def main(limit):
	sq = [d * d for d in range(10)]
	mem = [None] * limit
	mem[0] = False
	mem[1] = False
	mem[89] = True
	for n in range(limit):
		m = n
		while mem[m] == None:
			m = sum(sq[d] for d in digits(m))
		mem[n] = mem[m]
	return sum(mem)

if __name__ == '__main__':
	print(main(10000000)) # 8581146
