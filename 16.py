# Problem 16
power = 2
sum = 0
for i in range(1,1000):
  power *= 2
print(power)

for dig in str(power):
  sum += int(dig)
print(sum)