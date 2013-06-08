class Collatz(object):
	def __init__(self):
		self.mem = {1: 1}

	def chainLen(self, n):
		nums = []
		while n != 1:
			if n in self.mem:
				break
			nums.append(n)
			n = n // 2 if n % 2 == 0 else (3 * n + 1) // 2
		for m in reversed(nums):
			self.mem[m] = 1 + self.mem[n]
			n = m
		return self.mem[n]

def main(lim):
	collatz = Collatz()
	return max(range(1, lim), key=collatz.chainLen)

if __name__ == '__main__':
	print(main(1000000)) # 837799
