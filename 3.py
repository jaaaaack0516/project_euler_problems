# Problem 3

import math
# 600851475143
num = 600851475143
sqr = math.isqrt(num)
factors = []
primefactors = []

# finds every factor less than the square root of the given number
for x in range(1, sqr+1):
  if num%x == 0:
    factors.append(x)

# finds every factor greater than the square root of the given number
for x in reversed(range(len(factors))):
  y = int(num/factors[x])
  factors.append(y)

primefactors = factors
print(factors)


for x in range(len(factors)):
  z = 0
  for i in range(1, factors[x]+1):
    if z > 2:
      primefactors[x] = 0
      break
    elif factors[x]%i == 0:
      z += 1

while 0 in primefactors:
  primefactors.remove(0)

print(f"Prime factors of {num}: {primefactors}")
