# Problem 12
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

  factors *= 2
  if factors >= 500:
    print(sum)
    break

  print(f"num -> {x} sum -> {sum} factors {factors}")
  print(x)