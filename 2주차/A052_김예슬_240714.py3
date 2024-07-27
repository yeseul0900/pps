num = int(input())

for i in range(num):
  case = input()
  cnt_O = 0
  sum = 0
  for j in case:
    if j == "O":
      cnt_O += 1
    else:
      cnt_O = 0
    sum += cnt_O
  print(sum)