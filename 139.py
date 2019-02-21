# Consider a non-reducible pythagorean triple (a, b, c)
# We want c*c-2*a*b | c*c
# But c*c = a*a+b*b = (a-b)**2+2*a*b
# Therefore c*c-2*a*b = (b-a)**2
# Therefore we want (b-a) | c
# But c*c = a*a + b*b
# If k is a factor of c it must be a factor of a and b too
# But (a, b, c) is not reducible
# Therefore b-a=1
# Therefore a*a+(a+1)**2=c*c
# Therefore a = ((2*c*c-1)**.5-1)/2
# Therefore 2*c*c-1 must be some square d*d where a = (d-1)/2
# Therefore d*d-2*c*c=-1
# This is a negative Pell's equation for n=2
# Find integer solutions (d, c) to find the corresponding triangles (a, b, c)
# Note a+b+c = (d-1)/2+(d-1)/2+1+c = d+c
# The triangles are reduced so multiply perimeter by integers to reach target

def main(lim):
  d, c = 1, 1
  rv = 0
  while d+c < lim:
    d, c = 3*d+4*c, 2*d+3*c
    rv += lim // (d+c)
  return rv

if __name__ == '__main__':
  print(main(100000000))  # 10057761
