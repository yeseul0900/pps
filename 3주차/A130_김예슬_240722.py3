input_num = int(input())
num_list = []
for i in range(input_num):
  num = int(input())
  if num == 0:
    num_list.pop()
  else:
    num_list.append(num)
  
print(sum(num_list))