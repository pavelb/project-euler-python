from itertools import count

def main(m, limit):
	mem = [1] * m
	for n in count(m):
		F = 1 + mem[n - 1] + sum(mem[k] for k in range(n - m))
		if F > limit:
			return n
		mem.append(F)

print(main(50, 1000000)) # 168
