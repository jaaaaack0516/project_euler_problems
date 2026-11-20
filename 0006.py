# Problem 6 (Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum)

sumsqr = 0
sqrsum = 0

for i in range(1,101):
  sumsqr += (i*i)
  sqrsum += i

sqrsum *= sqrsum

print(sqrsum - sumsqr)
