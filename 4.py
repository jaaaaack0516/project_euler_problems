# Problem 4

pal = 1
for x in range(100,1000):
  for y in range(100,1000):
    sum = str(y * x)
    half1 = sum[:len(sum)//2]
    half2 = sum[len(sum)//2:][::-1]
    sum = int(sum)
    if half1 == half2 and sum > pal:
      pal = sum
print(pal)
