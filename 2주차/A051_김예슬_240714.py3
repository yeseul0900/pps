number = input()
al_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV','WXYZ']

time = 0
for i in number:
  for j in range(len(al_list)):
    if i in al_list[j]:
      time += j + 3
      break

print(time)