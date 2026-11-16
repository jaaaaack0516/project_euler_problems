# Problem 9

a = 0
b = 0
c = 0
fin = False

# counter = 0
while(True):
  # counter += 1
  b += 1
  for a in range (1, b):
    c = ((a*a) + (b*b))
    if c%1 == 0 and a+b+(c ** 0.5) == 1000:
      fin = True
      print(a*b*(c ** 0.5))
      break
  if fin == True:
    break
