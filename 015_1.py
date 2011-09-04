from lib import choose

def main(w, h):
	# trick: we are computing the pascal triangle
	return choose(w + h, w)

print(main(20, 20)) # 137846528820
