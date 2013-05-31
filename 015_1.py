from lib import choose

def main(w, h):
	# trick: we are computing the pascal triangle
	return choose(w + h, w)

if __name__ == '__main__':
	print(main(20, 20)) # 137846528820
