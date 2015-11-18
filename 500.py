from lib import Primes 
import heapq

primeGen = Primes()

def main(e, m):
  factors = list(map(primeGen.get, range(e)))
  heapq.heapify(factors)
  n = 1
  for _ in range(e):
    factor = factors[0]
    n = n * factor % m
    heapq.heappushpop(factors, factor ** 2)
  return n

if __name__ == '__main__':
  print(main(500500, 500500507))  # 35407281
