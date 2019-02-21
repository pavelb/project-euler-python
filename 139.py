# unfinished
from lib import pythagoreanTriples

# (b-a) | c
# a*a + b*b = k*k*(a-b)**2
# (a-b)**2+2*a*b = k*k*(a-b)**2
# 2*a*b = (k*k*-1)*(a-b)**2
for a, b, c in pythagoreanTriples():
    if a + b + c >= 1e8:
        break
    print(a+b+c, a, b, c)
