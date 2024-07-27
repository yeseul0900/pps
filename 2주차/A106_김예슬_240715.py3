num = int(input())
alphabet = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N' ,'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']

for i in range(num):
  char = input()
  sum = 0
  for j in range(len(alphabet)):
    if alphabet[j] not in char:
      sum += j + 65
  print(sum)