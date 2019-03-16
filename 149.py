from itertools import chain

def maxSubSum(a):
  maxSoFar = 0
  maxEndingHere = 0
  for n in a:
    maxEndingHere = max(0, maxEndingHere + n)
    maxSoFar = max(maxSoFar, maxEndingHere)
  return maxSoFar

def main():
  s=[0] * (2000**2+1)
  def get(row, col):
    return s[2000 * row + col + 1]
  for k in range(1, 2000**2 + 1):
    s[k] = 100003-200003*k+300007*k*k*k if k<56 else s[k-24]+s[k-55]+1000000
    s[k] = s[k]%1000000-500000
  return max(chain(
    # max of all rows
    (maxSubSum(get(row, col) for col in range(2000)) for row in range(2000)),
    # max of all columns
    (maxSubSum(get(row, col) for row in range(2000)) for col in range(2000)),
    # max of diagonals from top row
    (maxSubSum(get(i, col+i) for i in range(2000 - col)) for col in range(2000)),
    # max of anti-diagonals from top row
    (maxSubSum(get(i, col-i) for i in range(col + 1)) for col in range(2000)),
    # max of diagonals from left column
    (maxSubSum(get(row+i, i) for i in range(2000 - row)) for row in range(2000)),
    # max of anti-diagonals from right column
    (maxSubSum(get(row+i, 1999-i) for i in range(2000 - row)) for row in range(2000))
  ))

if __name__ == '__main__':
  print(main())  # 52852124
