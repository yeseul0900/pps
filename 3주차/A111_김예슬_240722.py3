num = int(input())
for i in range(num):
  input_num = int(input())
  count = 0
  while input_num:
    count = count * 2 + 1
    input_num = input_num - 1
  print(count)
  