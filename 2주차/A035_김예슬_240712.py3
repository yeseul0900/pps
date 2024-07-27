T = int(input())
Tlist = []
for i in range(T):
  seq = input().split()
  result = 0
  for j in range(len(seq)):
    if j == 0:
      result = float(seq[j])
    else:
      if seq[j] == "@":
        result = result * 3.0
      elif seq[j] == "%":
        result += 5.0
      else:
        result -= 7.0
  Tlist.append(result)
for i in Tlist:
  print(f'{i:.2f}')
      