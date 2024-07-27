num_p = int(input())
name_list = []
for i in range(num_p):
  input_name = input()
  name_list.append(input_name[0])

pop_list = []
for i in set(name_list):
  if name_list.count(i) > 4:
    pop_list.append(i)

if len(pop_list) == 0:
  print("PREDAJA")
else:
  string = ""
  for i in sorted(pop_list):
    string += i
  print(string)