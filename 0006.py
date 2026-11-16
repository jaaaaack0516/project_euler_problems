# Problem 6

sumsqr = 0
sqrsum = 0

for i in range(1,101):
  sumsqr += (i*i)
  sqrsum += i

sqrsum *= sqrsum
print(sumsqr)
print(sqrsum)

print(sqrsum - sumsqr)