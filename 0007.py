# Problem 7

primes = 0;
x = 1
while primes < 10001:
  x += 1
  f = 0
  for i in range(1,x+1):
    if x%i == 0:
      f += 1
    elif f > 3:
      break
  if f < 3:
    primes += 1
print(x)