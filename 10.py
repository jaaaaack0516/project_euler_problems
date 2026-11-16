# Problem 10

import math
sum = 0

for i in range(2,2000000):
  f = 0
  sum += i
  for x in range(2, math.isqrt(i)+1):
    if i%x == 0:
      f += 1
      sum -= i
      break
print(sum)