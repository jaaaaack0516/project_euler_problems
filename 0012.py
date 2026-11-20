# Problem 12 (Finds the value of the first triangle number to have over five hundred divisors)

import math

sum = 0
x = 0
factors = 0

while(True):
  sum = 0
  factors = 0
  x += 1

  for i in range (x+1):
    sum += i

  for f in range (1, math.isqrt(sum) + 1):
    if sum%f == 0:
      factors += 1

  if factors >= 250:
    print(sum)
    break
