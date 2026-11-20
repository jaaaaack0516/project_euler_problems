# Problem 7 (Finds the 10001st prime number)

primes = 0;
x = 1
while primes < 10001:
  x += 1
  f = 0
# Iterates through all numbers from 1 to current number and finds factors
  for i in range(1,x+1):
    if x%i == 0:
      f += 1
    elif f > 3:
      break
# Adds 1 to primes if current number is prime
  if f < 3:
    primes += 1
print(x)
