# Use Lagrange multipliers
# maximize f(x_1,x_2,...x_m) = prod_i=1^m x_i^{x_i}
# subject to g(x_1,x_2,...x_m) = -m + sum_i^m x_i = 0
# so we need df/d{x_i} = L * dg/d{x_i}
# f*i/x_i = L -> x_i = f*i/L
# Now g = 0 -> sum_i^m x_i = m
#           -> sum_i^m f*i/L = m
#           -> f/L*sum_i^m i = m
#           -> f/L*m*(m+1)/2 = m
#           -> f*(m+1)/2 = L
# Therefore x_i = f*i/L
#               = f*i/(f*(m+1)/2)
#               = 2*i/(m+1)

def P(m):
  p = 1 
  for i in range(1, m + 1): 
    p *= (2 * i / (m + 1))**i
  return p 


def main(a, b):
  return sum(int(P(m)) for m in range(a, b + 1))


if __name__ == '__main__':
  print(main(2, 15))  # 371048281
