num = int(input())
for i in range(num):
  input_num = int(input())
  reverse_num = int(str(input_num)[::-1])
  sum = input_num + reverse_num
  if str(sum) == str(sum)[::-1]:
    print("YES")
  else:
    print("NO")