from lib import digits

def main(lim):
	return max(sum(digits(pow(a, b))) for a in range(lim) for b in range(lim))

if __name__ == '__main__':
	print(main(100)) # 972
