# Problem 14 (Finds the starting number under one million that produces the longest collatz sequence)

seq = []
blegh = 0
min = 0
start = 0
n = 0
# 1000001
while n <= 1000001:
  seq = []
  n += 1
  blegh = n
  seq.append(blegh)
  while(True):
    if blegh == 1:
      break
    elif blegh%2 == 0:
      blegh = (int) (blegh / 2)
      seq.append(blegh)
    elif blegh%2 != 0:
      blegh = (int) (3 * blegh) + 1
      seq.append(blegh)
  if min <= len(seq):
    min = len(seq)
    start = n
print(start)
