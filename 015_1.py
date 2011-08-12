from math import factorial

def choose(n, k):
	return factorial(n) // (factorial(n - k) * factorial(k))

def main(w, h):
	# trick: we are computing the pascal triangle
	return choose(w + h, w)

print(main(20, 20)) # 137846528820
