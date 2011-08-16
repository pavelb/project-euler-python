from lib import prevFarey

def main(f, n):
    return prevFarey(f, n)[0]

print(main((3, 7), 1000000)) # 428570
