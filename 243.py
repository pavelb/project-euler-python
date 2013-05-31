from lib import Primes
from itertools import count

prime = Primes()

def main(limit_num, limit_denom):
	R = lambda d: (prime.phi(d), d - 1)
	def good(d):
		num, denom = R(d)
		return num * limit_denom < limit_num * denom

	d = 1

	for n in count(2):
		d *= n
		if good(d): break

	min_d = d
	kernel = d

	for m in range(n, 1, -1):
		kernel //= m
		print("kernel: %d" % kernel)
		for k in count(2):
			d = kernel * k
			if d >= min_d: break
			if good(d):
				min_d = d
				print(d)
				break

# takes too long to terminate but comes up with the answer in a few minutes
if __name__ == '__main__':
	print(main(15499, 94744))  # 892371480
