# Problem 1 (Find the Sum of all the multiples of 3 or 5 below 1000)

a = 0

for x in range(1, 1000):
  if x%3 == 0 or x%5 == 0:
    a = a + x

print(a)