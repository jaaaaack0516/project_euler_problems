# Problem 5 (Find the smallest possible number that is evenly divisible by all numbers 1 to 20)

x = 0

# Adds 2520 to x each iteration since 2520 is the first number evenly divisible by all numbers 1 to 10
while(True):
  counter = 0
  x += 2520
  for y in range(1,21):
    if x%y == 0:
      counter += 1

  if counter == 20:
    print(x)
    break
