from lib import Primes

def isFactor(p):
    if p < 11:
        return False
    mem = set()
    r = 10
    while True:
        if r == 1:
            return True
        if r in mem:
            return False
        mem.add(r)
        r = pow(r, 10, p)

def main(limit):
    rv = 0
    for p in Primes(limit).gen():
        if p > limit:
            break
        if not isFactor(p):
            rv += p
    return rv

if __name__ == '__main__':
    print(main(100000))  # 453647705
