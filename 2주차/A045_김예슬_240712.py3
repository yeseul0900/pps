input_value = input().upper()
char_list = list(set(input_value))

num_list = []
for char in char_list:
  num_list.append(input_value.count(char))

if num_list.count(max(num_list)) > 1:
  print("?")
else:
  print(char_list[num_list.index(max(num_list))])
