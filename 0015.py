# Problem 15
r = int(input("Enter the amount of rows and columns (same number for both): "))
n = r*2

num1 = 1
num2 = 1
num3 = 1

for i in range(1, n+1):
  num1 *= i
for i in range(1, r+1):
  num2 *= i
for i in range(1, (n-r)+1):
  num3 *= i
print(f"Combinations: {int(num1/(num2*num3))}")