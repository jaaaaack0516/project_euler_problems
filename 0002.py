# Problem 2 (Find the sum of all even valued terms in the Fibonacci sequence that do not exceed four million)

a = 1
b = 2
c = 0
sum = 0

while a <= 4000000:
  if a%2 == 0:
    sum = sum + a
  print(a)
  c = a + b
  a = b
  b = c

print('Sum: ' + str(sum))