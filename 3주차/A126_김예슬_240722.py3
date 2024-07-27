input_num = int(input())
if input_num < 100:
  print(input_num)
else:
  count = 99
  for i in range(100, input_num + 1):
    if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
      count += 1
  print(count)