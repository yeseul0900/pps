def sepeprate_num(num):
  k = 0
  for i in range(2, num+1):
    if num % i == 0:
      print(i)
      k = i
      break
  return k
num = int(input())
while(1):
  if num <= 1:
    break
  k = sepeprate_num(num)
  if k == num:
    break
  else:
    num = num // k