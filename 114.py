def main(m, blocks):
	mem = [0] * (blocks + 1)
	for n in range(m):
		mem[n] = 1
	for n in range(m, blocks + 1):
		mem[n] = 1 + mem[n - 1] + sum(mem[k] for k in range(n - m))
	return mem[blocks]

if __name__ == '__main__':
	print(main(3, 50)) # 16475640049
