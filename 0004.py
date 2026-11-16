# Problem 4 (Find the largest palindrome made from the product of two 3-digit numbers)

pal = 0

# first integer iterates from 100 to 999
for x in range(100,1000):
  # second integer iterates from 100 to 999
  for y in range(100,1000):
    # sums both integers then checks if that sum is a palindrome and greater than the last palindrome
    sum = str(y * x)
    half1 = sum[:len(sum)//2]
    half2 = sum[len(sum)//2:][::-1]
    sum = int(sum)
    
    if half1 == half2 and sum > pal:
      pal = sum
print(pal)