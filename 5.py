# Problem 5

x = 0
while(True):
  counter = 0
  x += 2520
  for y in range(1,21):
    if x%y == 0:
      counter += 1
  # print(x)
  if counter == 20:
    print(x)
    break
