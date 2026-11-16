# Problem 17
total = 0

def th_letters(th):
  let = 0
  if th == 1:
    let += 11
  return let

def h_letters(h,t,o):
  let = 0
  if h == 1 or h == 2 or h == 6:
    let += 10
  elif h == 4 or h == 5 or h == 9:
    let += 11
  elif h == 3 or h == 7 or h == 8:
    let += 12
  if h > 0 and t > 0 or h > 0 and o > 0:
    let += 3
  return let

def t_letters(t):
  let = 0
  if t == 4 or t == 5 or t == 6:
    let += 5
  elif t == 7:
    let += 7
  elif t != 0:
    let += 6
  return let

def o_letters(o):
  let = 0
  if o == 1 or o == 2 or o == 6 or o == 10:
    let = 3
  elif o == 4 or o == 5 or o == 9:
    let += 4
  elif o == 3 or o == 7 or o == 8:
    let += 5
  elif o == 11 or o == 12:
    let += 6
  elif o == 15 or o == 16:
    let += 7
  elif o == 13 or o == 14 or o == 18 or o == 19:
    let += 8
  elif o == 17:
    let += 9
  return let

def letters(num):
  temp = num
  thou = 0
  hund = 0
  tens = 0
  ones = 0

  while(temp > 0):
    if temp >= 1000:
      temp -= 1000
      thou += 1
    elif temp >= 100:
      temp -= 100
      hund += 1
    elif temp >= 20:
      while(temp > 0):
        if temp > 9:
          temp -= 10
          tens += 1
        else:
          temp -= 1
          ones += 1
    elif temp >= 1:
      temp -= 1
      ones += 1
  return th_letters(thou) + h_letters(hund, tens, ones) + t_letters(tens) + o_letters(ones)


for i in range(1,1001):
  total += letters(i)

print(total)