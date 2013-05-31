from lib import prevFarey

def main(left, right, n):
	count = -1
	while left != right:
		right = prevFarey(right, n)
		count += 1
	return count

if __name__ == '__main__':
	print(main((1, 3), (1, 2), 12000)) # 7295372
