from itertools import count

# Eq for number of blocks in m-th layer of cuboid (a,b,c)
def N(a, b, c, m):
  return 2*(a*b+b*c+c*a)+4*(m-1)*(a+b+c+m-2)

def C(n):
  if n % 2: return 0
  rv = 0 
  for a in count(1):
    if N(a, 1, 1, 1) > n:
      break
    for b in range(1, a + 1):
      if N(a, b, 1, 1) > n:
        break
      for c in range(1, b + 1):
        if N(a, b, c, 1) > n:
          break
        m = (int((a*a-2*a+b*b-2*b+c*c-2*c+n+1)**.5)-a-b-c+3)//2
        if m >= 1 and N(a, b, c, m) == n:
          rv += 1
  return rv

def main(lim):
  for n in count(0):
    num = C(n)
    if num == lim:
      return n
    print(n, num)

if __name__ == '__main__':
  print(main(1000))
