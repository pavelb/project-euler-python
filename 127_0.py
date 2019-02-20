# unfinished
from lib import Primes, multiply

def rad(n):
  return multiply(p for p, _ in primes.factors(n))

def aa(nums, limit):
  yield 1
  ws = []
  for n in nums:
    nw = []
    for a in [1] + ws:
      while True:
        a *= n
        if a > limit // 2:
          break
        yield a
        nw.append(a)
    if not nw:
      return
    ws = nw

def dpf(n):
  return set(p for p, _ in primes.factors(n))

primes = Primes()

def main(limit):
  hits = set()
  for c in range(limit):
    f = list(primes.factors(c))
    R = multiply(p**(n-1) for p, n in f)
    badf = set(p for p, _ in f)
    for a in aa((p for p in primes.gen() if p not in badf), c):
      b = c - a
      if a < b and rad(a)*rad(b) < R and dpf(b).isdisjoint(dpf(a) | badf):
        hits.add((a, b, c))
  return sum(c for _, _, c in hits)

if __name__ == '__main__':
  print(main(1000))  # 18407904

c = 9
for a in aa((p for p in primes.gen() if p not in dpf(c)), c):
  print(a)
