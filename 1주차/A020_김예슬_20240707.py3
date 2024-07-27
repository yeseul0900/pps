max = 0
for i in range(4):
  train_num = list(map(int, input().split()))
  if i == 0:
    temp = train_num[0]
    temp += train_num[1]
  else:
    temp -= train_num[0]
    temp += train_num[1]
  if temp > max:
    max = temp

print(max)