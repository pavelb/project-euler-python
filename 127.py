from lib import Primes, multiply

def rad(n):
  return multiply(p for p, _ in primes.factors(n))

def sec(nums, limit):
  ws = [(1, [])]
  for n in nums:
    nw = [(p*n, s + [n]) for p, s in ws if p*n <= limit]
    if not nw:
      break
    ws = ws + nw
  for _, s in ws:
    if len(s) > 0:
      yield set(s)

def dpf(n):
  return set(p for p, _ in primes.factors(n))

primes = Primes()

def main(limit):
  hits = set()
  for c in range(limit):
    f = list(primes.factors(c))
    R = multiply(p**(n-1) for p, n in f)
    badf = set(p for p, _ in f)
    for secs in sec((p for p in primes.gen() if p not in badf), R):
      ws = [1]
      for n in secs:
        nw = []
        for a in ws:
          while a < c:
            nw.append(a)
            a *= n
        ws = nw
      for a in ws:
        b = c - a
        if a < b and rad(a)*rad(b) < R and dpf(b).isdisjoint(dpf(a) | badf):
          hits.add((a, b, c))
  return sum(c for _, _, c in hits)

if __name__ == '__main__':
  print(main(120000))  # 18407904
