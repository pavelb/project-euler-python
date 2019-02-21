# Consider a pythagorean triple (a, b, c)
# We want c*c-2*a*b | c*c
# But c*c = a*a+b*b = (a-b)**2+2*a*b
# Therefore c*c-2*a*b = (b-a)**2
# We want (b-a) | c
# Let k=b-a so that c = m*k
# Therefore a*a+(a+k)**2=m*m*k*k
# Solving for a gives a = k*((2*m*m-1)**.5-1)/2
# 2*m*m-1 must be some square d*d making a = k*(d-1)/2
# This gives equation d*d-2*m*m=-1
# This is a negative Pell's equation for n=2
# Find integer solutions (d, m) to find the corresponding triangles (a, b, c)
# Note a+b+c = k*(d-1)/2 + k*(d-1)/2 + k + k*m = k*(d+m)
# Use unique solutions (d, m) then multiply by all integers k to reach target
# Or simply count how many such integers exist by dividing lim by (d+m)

def main(lim):
  d, m = 1, 1
  rv = 0
  while d+m < lim:
    d, m = 3*d+4*m, 2*d+3*m
    rv += lim // (d+m)
  return rv

if __name__ == '__main__':
  print(main(100000000))  # 10057761
